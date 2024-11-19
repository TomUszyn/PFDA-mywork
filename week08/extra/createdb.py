""" Create a database named wsaa. """
import mysql.connector

connection = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = connection.cursor()

mycursor.execute("create DATABASE wsaa")

mycursor.close()
connection.close()
