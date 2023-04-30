import mysql.connector
import sys
from mysql.connector import MySQLConnection, Error

#carts need to add items, remove items, display the items to the user, and get the item total from the user id
class cart:
    def _init_ (self):
        self.userid = 0
        self.quantity = 0
        self.total = 0 
        self.cartids = []

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

            print("Successful connection.")

        except:
            print("Failed connection.")

            ## exits the program if unsuccessful
        
        print()

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
        data = cartid,self.userid, itemID, amount, totalvalue

        try:
            cursor.execute(query, data)
            connection.commit()
            print(cursor.rowcount, "record inserted.")
            print()
        
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

            print("Successful connection.")

        except:
            print("Failed connection.")

            ## exits the program if unsuccessful
        
        print()

        cursor = connection.cursor()

        try:
            cursor.execute("DELETE FROM cart WHERE cartID=%s",pos)
            ## commits to database
            ## **needed** for changes to be made to a table
            connection.commit()
            return True
        except:
            return False

    def display(self, userID):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="password",
                database="projectschema"
            )

            print("Successful connection.")
        except:
            print("Failed connection.")

            ## exits the program if unsuccessful
        
        print()

        cursor = connection.cursor()
        
        cursor.execute("SELECT cartID, UserIDs, itemIDs, quantity, value from cart WHERE UserIDs=%s",userID)

        cartresults = cursor.fetchall()   

        row = 0 
        for x in cartresults:
            self.cartids += x[1]
            cursor.execute("SELECT title from inventory WHERE ItemID=%s",x[2])

            inventoryresults = cursor.fetchall()

            print(row + ". " + x[3]+"x"+ inventoryresults +"$"+x[4] )
        
        cursor.close()
        connection.close()

    def getcarttotal(self, userID):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="password",
                database="projectschema"
            )

            print("Successful connection.")

        except:
            print("Failed connection.")

            ## exits the program if unsuccessful
        
        print()

        cursor = connection.cursor()
        
        totalprice = 0
        for x in self.cartids:
            cursor.execute("SELECT price from cart WHERE cartID=%s",x[2])
            
            results = cursor.fetchall()
            
            totalprice += results

        return totalprice
    
    def checkout(self):




    





