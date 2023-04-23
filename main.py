from user import User
#from cart import Cart
#from user import User
#1from inventory import Inventory

import mysql.connector
import sys
import os

user = User()



def store():
    
    mainstoreloop = 1
    while(mainstoreloop != 0):
        os.system("cls")
        print("0. Exit")
        print("1. Store")
        print("2. Cart")
        print("3. Log Off")
        mainstoreloop = input("Select Menu Option: ")
    
        if(mainstoreloop == "0"):
            sys.exit()
        elif(mainstoreloop == "1"):
            print("store")
        elif(mainstoreloop == "2"):
            print("Cart")
        elif(mainstoreloop == "3"):
            main()

def main():
    while(1):
        os.system("cls")
        print("0. Exit")
        print("1. Login")

        option = input("Select Menu option: ")
    
        if (option == "0"):
            sys.exit()
    
        elif (option == "1"):
            username = input("Username: ")
            user.setusername(username)
            password = input("Password: ")
            user.setpassword(password)
  
            confirmation = input("Are you sure you want to login? (Y/N) ")
    
            if (confirmation.upper() == "Y"):
                status = user.loginaccount()
                if (status == True):
                    print("Logging in")
                    store()
                else:
                    continue
            else:
                print("Returning to menu.")

if __name__ == "__main__":
    main()
