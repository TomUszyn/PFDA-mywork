""" Select more complicated queries with parameters """
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="wsaa"
)

cursor = db.cursor()
SQL = "SELECT * FROM student WHERE name LIKE %s and age > 22"
values = ("%a%",)

cursor.execute(SQL, values)
result = cursor.fetchall()
for x in result:
    print(x)

db.close()
cursor.close()
