""" Inserting data into a database using Python """
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="wsaa"
)

cursor = db.cursor()
SQL = "insert into student (name, age) values (%s,%s)"
values = ("Joe",22)

cursor.execute(SQL, values)

db.commit()
print("1 record inserted, ID:", cursor.lastrowid)

db.close()
cursor.close()
