import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="utkarshR@01"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE python_db_1") # Query for creating a database

mycursor.execute("SHOW DATABASES") # Query for showing a database

for x in mycursor: 
    print("List of databases :- ", x) # loop through all the databases