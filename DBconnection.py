#Install the mysql-connector through pip in command line -> $ pip install mysql-connector
#import the mysql connector

import mysql.connector

#connecting database

mydb = mysql.connector.connect(host="localhost", user="YOUR_USERNAME", passwd="YOUR_PASSWORD", database="DATABASE_NAME")

#initialize cursor object

mycursor = mydb.cursor()

#mycursor.execute("show databases")

mycursor.execute("select * from student") 

#-> for fetching all values intable use

result = mycursor.fetchall()

#result = mycursor.fetchone()

for i in result:
    print(i)
