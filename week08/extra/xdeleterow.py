""" Delete a row from the table """
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="wsaa"
)

cursor = db.cursor()
SQL = "DELETE FROM student WHERE id = %s"
values = (2,)

cursor.execute(SQL, values)

db.commit()
print("delete done")

db.close()
cursor.close()
