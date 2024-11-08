import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Karthika@123',
    port='3306',

)
print(mydb)
obj = mydb.cursor()
#obj.execute("create database new_database")
obj.execute("show databases")
for i in obj:
    print(i)

