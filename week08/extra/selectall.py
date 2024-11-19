""" Select all data from student table """
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="wsaa"
)

cursor = db.cursor()
SQL = "SELECT * FROM student"
cursor.execute(SQL)
result = cursor.fetchall()
for x in result:
    print(x)

db.close()
cursor.close()
