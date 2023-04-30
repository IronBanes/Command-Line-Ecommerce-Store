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
        headers = ['ID', 'Stock', 'Title', 'Genre', 'Publisher', 'Price']
        table = []
        table.append(headers)
        for row in result:
            table.append(row)
        return table
    


    def display_items(self):
        items = self.list_items()
        headers = ['Title', 'Publisher', 'Stock', 'Price']
        print('{:<30}{:<30}{:<10}${:<10}'.format(*headers))
    
        for row in items[1:]:
            print('{:<30}{:<30}{:<10}'.format(row[2], row[4], row[1]))
    
    
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
    




   

        

