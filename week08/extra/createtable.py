""" Create a table in the database """
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="wsaa"
)

mycursor = mydb.cursor()
SQL="CREATE TABLE student (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(250), age INT)"

mycursor.execute(SQL)

mycursor.close()
mydb.close()
