import mysql.connector
import sys
import os    
class Inventory:
    def __init__(self):
        self.itemID = ""
        self.stock = ""
        self.title = ""
        self.genre = ""
        self.publisher = ""
        self.price = ""

        
    def setitemID(self, itemID):
        self.itemID = itemID
    
    def setstock(self, stock):
        self.stock = stock

    def settitle(self, title):
        self.title = title
    
    def setgenre(self, genre):
        self.genre = genre

    def setpublisher(self, publisher):
        self.publisher = publisher

    def setprice(self, price):
        self.price = price
 
   
   
    def getitemID(self, itemID):
        self.itemID = itemID
    
    def getstock(self, stock):
        self.stock = stock

    def gettitle(self, title):
        self.title = title
    
    def getgenre(self, genre):
        self.genre = genre

    def getpublisher(self, publisher):
        self.publisher = publisher

    def getprice(self, price):
        self.price = price


    def items(self):

        connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="password",
                database="projectschema"
            )
        
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM inventory")

        result = cursor.fetchall()

        for x in result:
            print("Entire Row:",x,"\n")



   

        

