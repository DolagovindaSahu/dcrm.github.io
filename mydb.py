#Install MYsql on your computer
#htttp://dev .mysql.com/downloads/installer/
#set the environment in a folder
#activate the environment in that folder
#pip install mysql
#pip install myql-connector
#pip install myql-connector-python

import mysql.connector

dataBase =mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = '1234'
	)

#prepare a cursor object
cursorObject = dataBase.cursor()

#create database
cursorObject.execute("CREATE DATABASE elderco")

print("All Done")

#Run this file -- > it will create a database in mysql.
#go to mysql workbanch to see the database. it requires to make a connection create a mysql database for once.