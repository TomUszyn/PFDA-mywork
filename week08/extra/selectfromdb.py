""" Select data from database using parameterized query """
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="wsaa"
)

cursor = db.cursor()
SQL = "SELECT * FROM student WHERE id = %s"
values = (1,)

cursor.execute(SQL, values)
result = cursor.fetchall()
for x in result:
    print(x)

db.close()
cursor.close()
