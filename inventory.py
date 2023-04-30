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
    
inventory = Inventory('localhost','username', 'password', 'inventory')
items = inventory.list_items()
for row in items:
    print(items)



   

        

