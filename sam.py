import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    database="vishal",
    password="1234"
    )


print(mydb)
mycursor = mydb.cursor()
mycursor.execute("create database bhavani_m")

for x in mycursor:   
    print(x)
