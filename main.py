from login import Login
#from cart import Cart
#from user import User
#1from inventory import Inventory

import mysql.connector
import sys

login = Login()

  
while(1):
    print("0. Exit")
    print("1. Login")
    print("2. Create Account")
    option = int(input("Select Menu option: "))
    if (option == 0):
        sys.exit()
    elif (option == 1):
        username = input("Username: ")
        login.setusername(username)
        password = input("Password: ")
        login.setpassword(password)
  
        confirmation = input("Are you sure you want to login? (Y/N) ")
        if (confirmation.upper() == "Y"):
            print("Login")
            login.loginaccount()
        else:
            print("Returning to menu.")
    elif (option == 2):
        username = input("Username: ")
        password = input("Password: ")
    
        