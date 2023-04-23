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
        self.email = ""
        
    def setfirstname(self, firstname):
        self.firstname = ""
        
    def setlastname(self, lastname): 
        self.lastname = ""
    

    def loginaccount(self):
        if(self.username == "IronBanes"):
            if(self.password == "password"):
                return True
            else:
                return False
        else:
            return False

    


