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
    
    def setemail(self, email):
        self.email = ""
        
    def setfirstname(self, firstname):
        self.firstname = ""
        
    def setlastname(self, lastname): 
        self.lastname = ""
    




    def loginaccount(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="password",
                database="projectschema"
            )

        except:
            print("Failed connection. Database is not open.")

            ## exits the program if unsuccessful
            sys.exit()
        cursor = connection.cursor()

        cursor.execute("SELECT username FROM users")
        
        result = cursor.fetchall()
        
        print("Enter result set: ", result, sep="\n", end="\n\n\n")


        print(self.username,self.password)


    def createaccount(self):
        pass


