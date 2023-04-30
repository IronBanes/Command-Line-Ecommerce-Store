from user import User
from cart import Cart
#from user import User
from inventory import Inventory

import mysql.connector
import sys
import os

user = User()
inventory = Inventory()
cart = Cart()

def cartmenu(returnloop):
    while(1):
        print("0. Exit")
        print("1. Back to Previous Menu")
        print("2. Show Cart")
        print("3. Remove Item from Cart")
        print("4. Check Out")

        cartloop = input("Select Menu Option: ")

        match inventory:
            case "0":
                print("Thank you for shopping with us")
                print("Have a Good Day")
                sys.exit()
            case "1":
                if(returnloop == 1):
                    store()
                elif(returnloop == 2):
                    invstore()
            case "2":
                print("These are the items in your cart: ")
                cart.display()
            case "3":
                print("What item would you like to remove from the cart?")
                cartnum = input("Enter the number of the item you want to remove form the cart: ")
                if(cart.remove(cartnum) == True):
                    print("The item has been removed")
                else:
                    print("The item was not in the cart please try again.")

            case "4":
                cart.display()

                cart.setuserid(user.userid)

                print("Your Grand Total is: ", cart.getcarttotal())
                option = input(("Are you sure you want to check out?(y/n)"))
                
                if(option == "y"):
                    cart.checkout()
                else:
                    continue
            

def invstore():
    while(1):
        print("Welcome "+ user.firstname+" to our store.")
        
        print("0. Exit")
        print("1. Back to Main Menu")
        print("2. List Items")
        print("3. Add Item to Cart")
        print("4. Look at Cart")
        print("5. Check Out")
        
        invstoreloop = input("Select Menu Option: ")

        match(invstoreloop):
            case "0":
                print("Thank you for shopping with us")
                print("Have a Good Day")
                sys.exit()
            
            case "1":
                print("Returning to Main Menu.")
                store()
            
            case "2":
                print("Our Inventory: ")
                inventory.display_items()
            
            case "3":
                print("What Game would you like to add to your cart?")
                gameNumber = input("Enter the number of the game: ")
                
                amount = input("How many copies of " + inventory.gettitle(gameNumber) + "?")
                if(amount < inventory.getstockcount(gameNumber)):
                    cart.additem(gameNumber,amount)
                else:
                    print("The amount you entered is more than we have in stock sorry.")
            
            case "4":
                cartmenu(2)
            
            case "5":
                cart.checkout()

def manageaccount():
    while (1):
        #os.system("cls")

        print("Hello "+ user.firstname+" how would you like to change your account info today?")

        print("0. Back to Main Menu")
        print("1. Change First Name")
        print("2. Change Last Name")
        print("3. Change Username")
        print("4. Change Password")
        print("5. Change Email")
        print("6. Change Shipping Information")
        print("7. Change Payment Information")
        manageacc = input("Select Menu Option: ")

        if(manageacc == "0"):
            store()

        elif(manageacc == "1"):#first name
            print("The current first name is ",user.getfirstname())
            newfirstname = input("What would you like to change it to: ")
            user.setfirstname(newfirstname)
            print("The First Name has been changed")

        elif(manageacc == "2"):#last name
            print("The current last name is ",user.getlastname())
            newlastname = input("What would you like to change it to: ")
            user.setlastname(newlastname)
            print("The Last Name has been changed")

        elif(manageacc == "3"):#username
            print("The current Username is ",user.getusername())
            newusername = input("What would you like to change it to: ")
            user.setlastname(newusername)
            print("The Username has been changed")

        elif(manageacc == "4"):#password
            oldpassword = input("Enter current password: ")
            newpassword = input("Enter new password: ")
            if(oldpassword == user.getpassword):
                user.setpassword(newpassword)
                print("Password has been changed")
            else:
                print("The password you enter does not match the current user password.")

        elif(manageacc == "5"):#email
            print("The current Email is ",user.getemail())
            newemail = input("What would you like to change it to: ")
            user.setemail(newemail)
            print("The Email has been changed")

        elif(manageacc == "6"):#shipping info
            if(user.getpaymentinfo):
                print("Your current Shipping information.")
                print("Address: ",user.getaddress())
                print("City: ",user.getcity())
                print("State: ",user.getstate())
                print("Zipcode: ",user.getzipcode())
                print()
                print("Please enter your new Shipping information")
            else:
                print("Please enter your Shipping information")

            address = input("Address: ")
            city = input("City: ")
            state = input("State: ")
            zipcode = input("Zipcode: ")
            user.setshippinginfo(address, city, state, zipcode)
            print("Shipping information has been changed.")


        elif(manageacc == "7"):#payment info
            if(user.getpaymentinfo):
                print("Your current card information.")
                print("Card:",user.getcard())
                print("CVV:", user.getcvv())
                print()
                print("Please enter your new card information")
            else:
                print("Please enter your card information")

            card = input("Card: ")
            cvv = input("CVV: ")
            user.setpaymentinfo(card, cvv)
            print("Payment information has been changed.")

def store():
    while(1):
        #os.system("cls")
        print("Hello "+ user.firstname+" how may we help you today.")

        print("0. Exit")
        print("1. Store")
        print("2. Cart")
        print("3. Manage Account")
        mainstoreloop = input("Select Menu Option: ")
    
        if(mainstoreloop == "0"):
            print("Thank you for shopping with us")
            print("Have a Good Day")
            sys.exit()
        elif(mainstoreloop == "1"):
            invstore()
        elif(mainstoreloop == "2"):
            cartmenu(1)
        elif(mainstoreloop == "3"):
            manageaccount()

def main():
    while(1):
        #os.system("cls")
        print("0. Exit")
        print("1. Login")
        print("2. Create Account")
        print("3.   ")

        option = input("Select Menu option: ")
    
        if (option == "0"):
            print("Thank you for shopping with us")
            print("Have a Good Day")
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

        elif (option == "2"):

            username = input("Username: ")
            user.setusername(username)
            password = input("Password: ")
            user.setpassword(password)
            email = input("Email:")
            user.setemail(email)
            firstname = input("First Name: ")
            user.setfirstname(firstname)
            lastname = input("Last Name: ")
            user.setlastname(lastname)

            user.createaccount()
            store()

        elif (option == "3"):
            username = "iron"
            user.setusername(username)
            password = "pass"
            user.setpassword(password)
            email = "email"
            user.setemail(email)
            firstname = "gavin"
            user.setfirstname(firstname)
            lastname = "eley"
            user.setlastname(lastname)

            user.createaccount()
            store()


if __name__ == "__main__":
    main()
