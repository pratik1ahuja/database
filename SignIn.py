#!/usr/bin/python2

#mysql modeule for mariadb databse
import mysql.connector 
import os
import cgi

print "Content-type:text/html"
print ""

data=cgi.FieldStorage()

#to get name and pasword from user throw html page
Uname=data.getvalue("uname")
passw=data.getvalue("upass")

#to make connection with database
dbcon = mysql.connector.connect(user='root',password='123',host='localhost',database='pratik') 
 
#to perform action into database
cur = dbcon.cursor() 

#to check user name and password in databse
cur.execute("select * from login1 where name ='%s' and password='%s'" %(Uname,passw))
#to fetch to the query result in variable results
results=cur.fetchall()

if results:
	#to check details of user in existing user
	for i in results:
		redirectURL=  "http://192.168.43.242/website.html"
		print ('<html>')
		print ('<head>')
		print ('<meta http-equiv="refresh" content="0; url= '+str(redirectURL)+'" />')
		print ('</head>')
		print ('</html>')
else:
	redirectURL=  "http://192.168.43.242/signerror.html"
	print ('<html>')
	print ('<head>')
	print ('<meta http-equiv="refresh" content="0; url= '+str(redirectURL)+'" />')
	print ('</head>')
	print ('</html>')




