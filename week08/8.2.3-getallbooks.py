import sqlite3
con = sqlite3.connect("pfda.db")
cur = con.cursor()
for row in cur.execute("select * from book where ISBN like '112%'"):
    print (f"row{row}")
