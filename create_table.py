import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="utkarshR@01",
    database="python_db"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE test (name VARCHAR(255), address VARCHAR(255))") # Query to create a table

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print("list of tables :-", x)