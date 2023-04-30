import mysql.connector
import sys

#carts need to add items, remove items, display the items to the user, and get the item total from the user id
class cart:
    def _init_ (self):
        self.userid = 0
        self.quantity = 0
        self.total = 0 

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

        cursor.execute("SELECT ItemID, stockcount, price FROM inventory WHERE ItemID = ? ",itemID)

        result = cursor.fetchall()

        price = result[2]

        totalvalue = price * amount

        cursor.execute("SELECT cartID from cart")

        result = cursor.fetchall()

        cartid = 0 
        for x in result:
            cartid += 1



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



    def removeitem(self, itemID):
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


    def displaycart(self, userID):
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

    





