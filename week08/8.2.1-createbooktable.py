import sqlite3
con = sqlite3.connect('pfda.db') # Databese is called pfda.db
cur = con.cursor()

# Create a table called book
cur.execute("CREATE TABLE book (title, author, ISBN)")
print("Table created.")

con.close()