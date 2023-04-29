import mysql.connector
import sys



class User:

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
        self.email = email
        
    def setfirstname(self, firstname):
        self.firstname = firstname
        
    def setlastname(self, lastname): 
        self.lastname = lastname
    
    def getusername(self, username):
        self.username = username

    def getpassword(self, password):
        self.password = password
    
    def getemail(self, email):
        self.email = email
        
    def getfirstname(self, firstname):
        self.firstname = firstname
        
    def getlastname(self, lastname): 
        self.lastname = lastname

    def loginaccount(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="password",
                database="projectschema"
            )

            print("Successful connection.")

        except:
            print("Failed connection.")

            ## exits the program if unsuccessful
        
        print()

        cursor = connection.cursor()

        cursor.execute("SELECT UserIds, username, password FROM users")

        result = cursor.fetchall()

        for x in result:
            print("Entire Row:",x,"\n")
            if (x[1] == self.username and x[2] == self.password):
                self.userid = x[0]
                return True
            else:
                return False
        
    def createaccount(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="password",
                database="projectschema"
            )

            print("Successful connection.")

        except:
            print("Failed connection.")

            ## exits the program if unsuccessful
        
        print()
        cursor = connection.cursor()

        query = "INSERT INTO users (firstname, lastname, username, password, email) VALUES (%s,%s,%s,%s,%s,%s)"
        data = self.firstname + "," + self.lastname + "," + self.username + "," + self.password + "," + self.email

        cursor.execute(query, data)

        connection.commit()
        print(cursor.rowcount, "record inserted.")
        print()
        
        

