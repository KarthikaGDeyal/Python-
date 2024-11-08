import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Karthika@123',
    port='3306',
    database='new_database'
)

mycursor=mydb.cursor()
#mycursor.execute("create table Employee2(emp_id int primary key,name varchar(50),location varchar(50),company varchar(50),salary bigint,designation varchar(50))")
mycursor.execute('show tables')
for i in mycursor:
    print(i)
mycursor.execute("insert into Employee2 values(1,'nithya','cochin','TCS',30000,'Developer')")
mycursor.execute("insert into Employee2 values(2,'diya','cochin','TCS',40000,'Engineer')")
mycursor.execute("insert into Employee2 values(3,'ria','calicut','Infosys',25000,'Tester')")
mycursor.execute("insert into Employee2 values(4,'elena','calicut','luminar',32000,'HR')")
mycursor.execute("insert into Employee2 values(5,'laya','calicut','luminar',10000,'Intern')")
mycursor.execute("select * from Employee2")
for i in mycursor:
    print(i)
    print(type(i))

