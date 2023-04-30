import mysql.connector
from mysql.connector import MySQLConnection, Error
import sys
from datetime import date



class User:

    def __init__(self):
        self.username = ""
        self.password = ""
        self.email = ""
        self.firstname = ""
        self.lastname = ""
        self.userid = 0
        self.shippingid = 0
        self.card = ""
        self.cvv = ""
        self.address = ""
        self.city = ""
        self.state = ""
        self.zipcode = ""

    def getuserid(self):
        return self.userid
    
#region username
    def setusername(self, username):
        self.username = username
    
    def getusername(self):
        return self.username 
#endregion

#region password
    def setpassword(self, password):
        self.password = password
    
    def getpassword(self):
        return self.password 
#endregion

#region email
    def setemail(self, email):
        self.email = email

    def getemail(self):
        return self.email 
#endregion

#region firstname
    def setfirstname(self, firstname):
        self.firstname = firstname
        
    def getfirstname(self):
        return self.firstname 
#endregion   

#region lastname
    def setlastname(self, lastname): 
        self.lastname = lastname
      
    def getlastname(self): 
        return self.lastname 
#endregion

#region payment
    def getcard(self):
        return self.card
    
    def getcvv(self):
        return self.cvv
#endregion

#region shippinginfo
    def getaddress(self):
        return self.address

    def getcity(self):
        return self.city

    def getstate(self):
        return self.state

    def getzipcode(self):
        return self.zipcode
#endregion

#region login/create
    def loginaccount(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="password",
                database="projectschema"
            )
        except:
            print("Failed connection.")

            ## exits the program if unsuccessful

        cursor = connection.cursor()

        cursor.execute("SELECT UserIds, firstname, lastname, username, password, email FROM users")

        result = cursor.fetchall()

        for x in result:
            if (x[3] == self.username and x[4] == self.password):
                self.userid = x[0]
                self.firstname = x[1]
                self.lastname = x[2]
                self.username = x[3]
                self.password = x[4]
                self.email = x[5]

                return True
            else:
                return False
        cursor.close()
        connection.close()

    def createaccount(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="password",
                database="projectschema"
            )
        except:
            print("Failed connection.")

            ## exits the program if unsuccessful
        
        cursor = connection.cursor()

        cursor.execute("SELECT UserIds, username FROM users")

        result = cursor.fetchall()

        numofusers = 0
        for x in result:
            numofusers += 1
            if (x[1] == self.username):
                return False
        


        query = "INSERT INTO users (UserIDs, firstname, lastname, username, password, email) VALUES(%s, %s, %s, %s, %s, %s)"
        data = (numofusers + 1, self.firstname, self.lastname, self.username, self.password, self.email)
        self.userid = numofusers
        
        try:
            cursor.execute(query, data)
            connection.commit()
        
        except Error as error:
            print(error)
        finally:
            cursor.close()
            connection.close()
#endregion

    def setshippinginfo(self, address, city, state, zipcode):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="password",
                database="projectschema"
            )
        except:
            print("Failed connection.")

            ## exits the program if unsuccessful
        
        cursor = connection.cursor()

        cursor.execute("SELECT ShippingIDS, UserIDs FROM shipping")

        result = cursor.fetchall()

        numofshipids = 0
        userexist = False
        for x in result:
            numofshipids += 1
            if (x[1] == self.userid):
                userexist = True
                

        if(userexist):
            query ="UPDATE shipping SET address=%s, city=%s, state=%s, zipcode=%s WHERE UserIDs = %s" 
            data = ( address, city, state, zipcode, self.userid,)
        else:
            query =  "INSERT INTO shipping (ShippingIDs, UserIDs, address, city, state, zipcode) VALUES(%s, %s, %s, %s, %s)"
            data = (numofshipids + 1, self.userid, address, city, state, zipcode)

        try:
            cursor.execute(query, data)
            connection.commit()
            return True
        
        except Error as error:
            print(error)
        finally:
            cursor.close()
            connection.close()

    def setpaymentinfo(self, card, cvv):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="password",
                database="projectschema"
            )
        except:
            print("Failed connection.")

            ## exits the program if unsuccessful
        
        cursor = connection.cursor()

        cursor.execute("SELECT paymentID, UserIDs FROM payment")

        result = cursor.fetchall()

        numofpayment = 0
        userexist = False
        for x in result:
            numofpayment += 1
            if (x[1] == self.userid):
                userexist = True

        query = "INSERT INTO payment (paymentID, UserIDs, card, cvv) VALUES(%s, %s, %s, %s)"
        data = (numofpayment, self.userid, card, cvv)

        if(userexist):
            query ="UPDATE payement SET  card=%s, cvv=%s WHERE UserIDs = %s" 
            data = (card, cvv, self.userid)
        else:
            query =  "INSERT INTO payment (paymentID, UserIDs, card, cvv) VALUES(%s, %s, %s, %s)"
            data = (numofpayment + 1, self.userid, card, cvv)

        try:
            cursor.execute(query, data)
            connection.commit()
        
        except Error as error:
            print(error)
        finally:
            cursor.close()
            connection.close()

    def getpaymentinfo(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="password",
                database="projectschema"
            )
        except:
            print("Failed connection.")

            ## exits the program if unsuccessful
        
        cursor = connection.cursor()

        cursor.execute("SELECT paymentID, UserIDs, card, cvv FROM payment")

        result = cursor.fetchall()

        for x in result:
            if (x[1] == self.userid):
                self.card = x[3]
                self.cvv = x[4]
                cursor.close()
                connection.close()
                return True
            else:
                return False
        
    def getshippinginfo(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="password",
                database="projectschema"
            )
        except:
            print("Failed connection.")

            ## exits the program if unsuccessful
        
        cursor = connection.cursor()

        cursor.execute("SELECT ShippingIDS, UserIDs, address, city, state, zipcode FROM shipping")

        result = cursor.fetchall()

        for x in result:
            if (x[1] == self.userid):
                self.address = x[3]
                self.city = x[4]
                self.state = x[5]
                self.zipcode = x[6]
                cursor.close()
                connection.close()
                return True
            else:
                return False

    def setlastorder(self,orderdate):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="password",
                database="projectschema"
            )

            

        except:
            print("Failed connection.")

            ## exits the program if unsuccessful
        
        print()
        cursor = connection.cursor()
        today = date.today()
        cursor.execute("UPDATE users SET lastorderdate=%s WHERE UserIDs =%s",(today,self.userid))
        connection.commit()
        cursor.close()
        connection.close()

    def updateaccountinfo(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="password",
                database="projectschema"
            )
        except:
            print("Failed connection.")

            ## exits the program if unsuccessful
    
        cursor = connection.cursor()

        query ="UPDATE users SET firstname=%s, lastname=%s, username=%s, password=%s, email=%s WHERE UserIDs=%s" 
        data = (self.firstname, self.lastname, self.username, self.password, self.email, self.userid)

        try:
            cursor.execute(query, data)
            connection.commit()
        
        except Error as error:
            print(error)
        finally:
            cursor.close()
            connection.close()
        
    