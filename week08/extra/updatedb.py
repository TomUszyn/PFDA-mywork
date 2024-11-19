""" Update a record in the student table. """
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
 database="wsaa"
)

cursor = db.cursor()
SQL = "update student set name= %s, age=%s  where id = %s"
values = ("Maja",35, 3)

cursor.execute(SQL, values)

db.commit()
print("update done")

cursor.close()
db.close()
