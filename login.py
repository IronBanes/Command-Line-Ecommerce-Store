import mysql.connector
import sys
class Login:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.email = ""
        self.firstname = ""
        self.lastname = ""
        self.userid = ""
    
    def setusername(self, username):
        self.username = username

    def setpassword(self, password):
        self.password = password
    
    def loginaccount(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
            user="root",
            password="",
            database="methods"
            )

        except:
            print("Failed connection. Database is not open.")

            ## exits the program if unsuccessful
            sys.exit()
        cursor = connection.cursor()
        
        print(self.username,self.password)


    def createaccount(self):
        pass


