import mysql.connector
import sys
import os    
class Inventory:
    def __init__(self, host, user, password, database):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="projectschema"
            )
        
        self.cursor = self.connection.cursor()
    
    def list_items(self):

        self.cursor.execute("SELECT * FROM inventory")

        result = self.cursor.fetchall()

        return result
    
    def get_title(self, itemID):
        sql = "SELECT FROM title FROM inventory WHERE itemID = %s"
        value = (itemID,)
        self.cursor.execute(sql, value)
        title = self.cur.fetchone()[0]
        return title
    
    def get_stock(self, itemID):
        sql = "SELECT stock FROM inventory WHERE itemID = %s"
        value = (itemID,)
        self.cursor.execute(sql, value)
        stock = self.cur.fetchone()[0]
        return stock
    
inventory = Inventory('localhost','username', 'password', 'inventory')
items = inventory.list_items()
for row in items:
    print(items)



   

        

