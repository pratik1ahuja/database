#!/usr/bin/python2

#mysql modeule for mariadb databse
import mysql.connector 
 
#to make connection with database
dbcon = mysql.connector.connect(user='root',password='123',host='localhost',database='pratik') 
 
#to perform action into database
cur = dbcon.cursor() 

#to insert a value in existing table 
cur.execute("insert into login1(name,password)values('anand1','123')")

# To commit the changes in table
dbcon.commit()

# To select the data of the table
cur.execute("select * from login1")

#to print the table
for (name,password) in cur: 
      print("{}, {}".format(name,password))

#to close database for security purpose
dbcon.close()

