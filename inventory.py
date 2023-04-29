import mysql.connector
import sys
import os    
class Inventory:
    Game1 = "Halo 2"
    Game2 = "Titanfall 2"
    Game3 = "Super Mario Galaxy"
    Game4 = "Call of Duty 4"
    Game5 = "Need For Speed Hot Pursuit Remasterd"
    Game6 = "Super Smash Bros Ulitmate"
    Game7 = "Driver San Francisco"
    Game8 = "Legend of Zelda: Breath of the Wild"
    Game9 = "Sonic Frontiers"

    connection = mysql.connector.connect(
        host= "localhost",
        user= "root",
        passwd= "password",
        database= "projectschema",
    )
    
    cursor = connection.cursor()

    query = "INSERT INTO inventory (ItemID, stockcount, title, genre, publisher, price) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    data1 = 1123 + "," + 14 + "," + Game1 + "," + "Shooter" + "," + "Microsoft Game Studios" + 6.99
    data2 = 1223 + "," + 10 + "," + Game2 + "," + "Shooter" + "," + "Electronic Arts" + 6.99
    data3 = 1323 + "," + 5 + "," + Game3 + "," + "Platformer" + "," + "Nintendo" + 10.99
    data4 = 1423 + "," + 2 + "," + Game4 + "," + "Shooter" + "," + "Activision" + 4.99
    data5 = 1523 + "," + 20 + "," + Game5 + "," + "Racing" + "," + "Electronic Arts" + 19.99
    data6 = 1623 + "," + 15 + "," + Game6 + "," + "Fighting" + "," + "Nintendo" + 59.99
    data7 = 1723 + "," + 10 + "," + Game7 + "," + "Racing" + "," + "Ubisoft" + 9.99
    data8 = 1823 + "," + 15 + "," + Game8 + "," + "Adventure" + "," + "Nintendo" + 59.99
    data9 = 1923 + "," + 20 + "," + Game9 + "," + "Adventure" + "," + "Sega" + 59.99
    
    cursor.execute(query,data1)
    cursor.execute(query,data2)
    cursor.execute(query,data3)
    cursor.execute(query,data4)
    cursor.execute(query,data5)
    cursor.execute(query,data6)
    cursor.execute(query,data7)
    cursor.execute(query,data8)
    cursor.execute(query,data9)

    
    connection.commit()

    result = cursor.fetchall()

    print(result)



   

        

