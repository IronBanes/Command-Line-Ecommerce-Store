import mysql.connector
import sys
from mysql.connector import MySQLConnection, Error

#carts need to add items, remove items, display the items to the user, and get the item total from the user id
class Cart:
    def _init_ (self):
        self.userid = 0
        self.quantity = 0
        self.total = 0 
        self.lists = []

    def setuserid(self, userid):
        self.userid = userid

    def additem(self, itemID, amount):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="password",
                database="projectschema"
            )
        except:
            print("Failed connection.")

            ## exits the program if unsuccessful

        cursor = connection.cursor()

        #get Item
        cursor.execute("SELECT ItemID, price FROM inventory WHERE ItemID=? ", itemID)

        result = cursor.fetchall()

        price = result[2]

        totalvalue = price * amount

        #get cart list to find what the current id is 
        cursor.execute("SELECT cartID from cart")

        result = cursor.fetchall()

        cartid = 0 
        for x in result:
            cartid += 1
        
        
        #insert item into cart
        query = "INSERT INTO cart (cartID, UserIDs, itemIDs, quanity, value) VALUES(%s, %s, %s, %s, %s)"
        data = cartid + 1,self.userid, itemID, amount, totalvalue

        try:
            cursor.execute(query, data)
            connection.commit()        
        except Error as error:
            print(error)
        finally:
            cursor.close()
            connection.close()

    def removeitem(self, pos):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="password",
                database="projectschema"
            )
        except:
            print("Failed connection.")

            ## exits the program if unsuccessful
        
        cursor = connection.cursor()

        query = "SELECT cartID, UserIDs, itemIDs, quantity, value FROM cart WHERE UserIDs = %s"
        data = (self.userid,)
        cursor.execute(query, data)

        cartresults = cursor.fetchall()   
 
        cartlist = []
        for x in cartresults:
            cartid = x[0]
            cartlist.append(x[0])


        query = "DELETE FROM cart WHERE cartID = %s"
        data = (cartlist[int(pos)],)

        
        try:
            cursor.execute(query,data)
            ## commits to database
            ## **needed** for changes to be made to a table
            connection.commit()

            cursor.close()
            connection.close()
            return True
        except:
            cursor.close()
            connection.close()
            return False

    def display(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="password",
                database="projectschema"
            )
        except:
            print("Failed connection.")

            ## exits the program if unsuccessful
        
        print()

        cursor = connection.cursor()
        query = "SELECT cartID, UserIDs, itemIDs, quantity, value FROM cart WHERE UserIDs = %s"
        data = (self.userid,)
        cursor.execute(query, data)

        cartresults = cursor.fetchall()   

        row = 0 
        cartlist = []
        for x in cartresults:
            cartid = x[0]
            cartlist.append(x[0])
            query = "SELECT title from inventory WHERE ItemID = %s"
            data = (x[2],)
            cursor.execute(query,data)

            inventoryresults = cursor.fetchall()
            for y in inventoryresults:
                inv = y[0]
            print(row , ". " , x[3],"x", inv ,"$",x[4] )
            row += 1
        self.lists = cartlist
        cursor.close()
        connection.close()

    def getcarttotal(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="password",
                database="projectschema"
            )
        except:
            print("Failed connection.")

            ## exits the program if unsuccessful
        
        cursor = connection.cursor()
        
        totalprice = 0
        for x in self.lists:
            cursor.execute("SELECT value FROM cart WHERE cartID=%s",(x,))
            
            results = cursor.fetchall()
            totalprice += results[0][0]
        
        cursor.close()
        connection.close()

        return totalprice
    
    def checkout(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="password",
                database="projectschema"
            )
        except:
            print("Failed connection.")

            ## exits the program if unsuccessful
        
        cursor = connection.cursor()        

        query = "SELECT cartID, UserIDs, itemIDs, quantity, value FROM cart WHERE UserIDs = %s"
        data = (self.userid,)
        cursor.execute(query, data)

        cartresults = cursor.fetchall()   
 
        cartlist = []
        for x in cartresults:
            cartid = x[0]
            cartlist.append(x[0])


        for x in cartlist:
            cursor.execute("SELECT ItemIDs,quantity FROM cart WHERE cartID=%s",(x,))
            
            cartresults = cursor.fetchall()
            
            cursor.execute("SELECT stockcount FROM inventory WHERE ItemID=%s",(cartresults[0][0],))
            inventresults = cursor.fetchall()
            
            newstockcount = inventresults[0][0] - cartresults[0][1]
            cursor.execute("UPDATE inventory SET stockcount=%s WHERE ItemID = %s", (newstockcount, cartresults[0][0]))
            
            cursor.execute("DELETE FROM cart WHERE cartID=%s",(x,))
            
            connection.commit()
        
        cursor.close()
        connection.close()


        

    










