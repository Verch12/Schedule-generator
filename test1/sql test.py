import sqlite3

con = sqlite3.connect("lessons.db")
cursor = con.cursor()

#cursor.execute("INSERT INTO lessons ([teacher ID], priority, time, class) VALUES (?, ?, ?, ?)", (100, 0, 99, "99,98,97"))
cursor.execute("INSERT INTO lessons (teacherID, priority, time, class) VALUES (?, ?, ?, ?)", (100, 0, 99, "0"))
con.commit()
con.close()

#-----------------------------------------------------------------------

con = sqlite3.connect("lessons.db")
cursor = con.cursor()

cursor.execute("SELECT * FROM lessons")

rows = cursor.fetchall()

for row in rows:
    print(row)
print("")
con.close()

#-----------------------------------------------------------------------

con = sqlite3.connect("lessons.db")
cursor = con.cursor()

# Удаляем строку, где id = 3
cursor.execute("DELETE FROM lessons WHERE priority = ? AND teacherID = ? AND class = ?", (0, 100, "0"))

con.commit()
con.close()

#-----------------------------------------------------------------------

con = sqlite3.connect("lessons.db")
cursor = con.cursor()

cursor.execute("SELECT * FROM lessons")

rows = cursor.fetchall()

for row in rows:
    print(row)
print("")
con.close()