import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Karthika@123',
    port='3306',
    database='new_database'
)


mycursor = mydb.cursor()
mycursor.execute("create table Student(name varchar(50),age int,place varchar(50))")
mycursor.execute("Show Tables")
for i in mycursor:
    print(i)
mycursor.execute("insert into Student values('Anjana',21,'Cochin')")
mycursor.execute("select * from Student")
for i in mycursor:
    print(i)
    print(type(i))
