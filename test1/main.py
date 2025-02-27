import sqlite3

con = sqlite3.connect("lessons.db")
cursor = con.cursor()
cursor.execute("SELECT * FROM lessons")
lessons = cursor.fetchall()
cursor.execute("SELECT * FROM teacher")
teacher = cursor.fetchall()
con.close()

teachers = {}
for i in teacher:
    teacherID, nameTeacher, lesson, priority, classroom = i
    teachers[teacherID] = nameTeacher, lesson, priority, classroom

print("Придмет", "Кабинет", "Приоритет предмета", "количество уроков", "Класс")
for i in lessons:
    teacherID, priority, time, clas = i
    print(teachers[teacherID][1], teachers[teacherID][3], priority, time, clas)


#print(teachers)