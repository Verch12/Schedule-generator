import sqlite3

con = sqlite3.connect('lessons.db')
cur = con.cursor()
cur.execute("SELECT * FROM lessons")

for person in cur.fetchall():
    print(person[0], person[1], person[2], person[3], person[4])

con.close()