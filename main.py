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
        cart.setuserid(user.getuserid())
        print()
        print("0. Exit")
        print("1. Back to Previous Menu")
        print("2. Show Cart")
        print("3. Remove Item from Cart")
        print("4. Check Out")

        cartloop = input("Select Menu Option: ")

        match cartloop:
            case "0":
                print()
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
                cartnum = input("Enter the number of the item you want to remove from the cart: ")
                if(cart.removeitem(cartnum) == True):
                    print("The item has been removed")
                else:
                    print("The item was not in the cart please try again.")

            case "4":
                if(user.getshippinginfo() == False):
                    print()
                    print('You do not have a shipping address in our database could you please enter one for check out.')
                    address = input("Address: ")
                    city = input("City: ")
                    state = input("State: ")
                    zipcode = input("Zipcode: ")
                    user.setshippinginfo(address, city, state, zipcode)
                    
                else:
                    print()
                    shippingchange = input("You have an address on record would you like to use that shipping address? (y/n)")
                    if(shippingchange=="n"):
                        address = input("Address: ")
                        city = input("City: ")
                        state = input("State: ")
                        zipcode = input("Zipcode: ")
                        user.setshippinginfo(address, city, state, zipcode)
                    
                if(user.getpaymentinfo() == False):
                    print()
                    print('You do not have a Card with us could you please enter one for check out.')
                    card = input("Card: ")
                    cvv = input("CVV: ")
                    user.setpaymentinfo(card, cvv)
                else:
                    print()
                    cardchange = input("You have a card on record would you like to use that card? (y/n)")
                    if(cardchange=="n"):
                        card = input("Card: ")
                        cvv = input("CVV: ")
                        user.setpaymentinfo(card, cvv)
                    

                print("Your Cart:")
                print()
                cart.display()
                total = cart.getcarttotal()
                print("Your Grand Total is: $", total)
                option = input(("Are you sure you want to check out?(y/n)"))
                
                if(option == "y"):
                    cart.checkout()
                    user.setlastorder()
                    print("Your games will be shipped to "+user.getaddress()+".")
                    print("Thank you for shopping with us!")
                    store()

                       
def invstore():
    while(1):
        print()
        cart.setuserid(user.getuserid())
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
                print()
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
                if(user.getshippinginfo() == False):
                    print()
                    print('You do not have a shipping address in our database could you please enter one for check out.')
                    address = input("Address: ")
                    city = input("City: ")
                    state = input("State: ")
                    zipcode = input("Zipcode: ")
                    user.setshippinginfo(address, city, state, zipcode)
                else:
                    print()
                    shippingchange = input("You have an address on record would you like to use that shipping address? (y/n)")
                    if(shippingchange=="n"):
                        address = input("Address: ")
                        city = input("City: ")
                        state = input("State: ")
                        zipcode = input("Zipcode: ")
                        user.setshippinginfo(address, city, state, zipcode)
                    
                if(user.getpaymentinfo() == False):
                    print()
                    print('You do not have a Card with us could you please enter one for check out.')
                    card = input("Card: ")
                    cvv = input("CVV: ")
                    user.setpaymentinfo(card, cvv)
                else:
                    print()
                    cardchange = input("You have a card on record would you like to use that card? (y/n)")
                    if(cardchange=="n"):
                        card = input("Card: ")
                        cvv = input("CVV: ")
                        user.setpaymentinfo(card, cvv)
                    

                print("Your Cart:")
                print()
                cart.display()
                total = cart.getcarttotal()
                print("Your Grand Total is: $", total)
                option = input(("Are you sure you want to check out?(y/n)"))
                
                if(option == "y"):
                    cart.checkout()
                    user.setlastorder()
                    print("Your games will be shipped to "+user.getaddress()+".")
                    print("Thank you for shopping with us!")
                    store()

def manageaccount():
    while (1):
        #os.system("cls")
        print()

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
            user.updateaccountinfo()
            print("The First Name has been changed")

        elif(manageacc == "2"):#last name
            print("The current last name is ",user.getlastname())
            newlastname = input("What would you like to change it to: ")
            user.setlastname(newlastname)
            user.updateaccountinfo()
            print("The Last Name has been changed")

        elif(manageacc == "3"):#username
            print("The current Username is ",user.getusername())
            newusername = input("What would you like to change it to: ")
            user.setusername(newusername)
            user.updateaccountinfo()
            print("The Username has been changed")

        elif(manageacc == "4"):#password
            oldpassword = input("Enter current password: ")
            newpassword = input("Enter new password: ")
            if(oldpassword == user.getpassword()):
                user.setpassword(newpassword)
                user.updateaccountinfo()
                print("Password has been changed")
            else:
                print("The password you enter does not match the current user password.")

        elif(manageacc == "5"):#email
            print("The current Email is ",user.getemail())
            newemail = input("What would you like to change it to: ")
            user.setemail(newemail)
            user.updateaccountinfo()
            print("The Email has been changed")

        elif(manageacc == "6"):#shipping info
            if(user.getshippinginfo()):
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
            if(user.getpaymentinfo()):
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
        print()
        print("Hello "+ user.firstname+" how may we help you today.")

        print("0. Exit")
        print("1. Store")
        print("2. Cart")
        print("3. Manage Account")
        mainstoreloop = input("Select Menu Option: ")
    
        if(mainstoreloop == "0"):
            print()
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
        print()
        print("0. Exit")
        print("1. Login")
        print("2. Create Account")

        option = input("Select Menu option: ")
    
        if (option == "0"):
            print()
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
                    print("Username or password was incorrect please try again.")
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

if __name__ == "__main__":
    main()
