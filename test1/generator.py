import random

# Данные о предметах, кабинетах, приоритетах и количестве уроков
data = [
    ("Математика", 11, 0, 1, "5,10,11"),
    ("Биология", 12, 0, 1, "6,10,11"),
    ("Физика", 13, 0, 1, "7,11"),
    ("История", 14, 0, 1, "5,8,11"),
    ("География", 15, 0, 1, "7,9"),
    ("Русский язык", 16, 0, 1, "5,6,8,10"),
    ("Английский язык", 17, 0, 1, "5,6,7,9"),
    ("Химия", 18, 0, 1, "6,7,8,10"),
    ("Физкультура", 19, 0, 1, "5,6,7,8,9"),
    ("Музыка", 20, 0, 1, "8,9,10"),
    ("Труд", 21, 0, 1, "7,8,9,10"),
    ("География", 22, 0, 1, "5"),
    ("Русский язык", 23, 0, 1, "9,11"),
    ("Математика", 11, 1, 2, "10"),
    ("Физика", 13, 1, 2, "7,11"),
    ("Русский язык", 16, 1, 2, "5"),
    ("Химия", 18, 1, 2, "6"),
    ("Физкультура", 19, 1, 2, "7"),
    ("Музыка", 20, 1, 2, "9")
]

# Функция генерации расписания
def generate_schedule(cell_width=22, length=[5, 12]):
    # Создаём структуру данных для расписания
    schedule = {grade: {} for grade in range(length[0], length[1])}

    # Заполняем расписание предметами с их количеством уроков
    for subject, cabinet, priority, lessons, classes in data:
        for grade in classes.split(','):
            grade = int(grade)
            if subject not in schedule[grade]:
                schedule[grade][subject] = {"cabinet": cabinet, "remaining": lessons}

    daily_schedule = {grade: [''] * 6 for grade in range(length[0], length[1])}  # 6 уроков в день

    # Заполняем расписание поурочно
    for lesson_index in range(length[0]+1):
        used_subjects = set()  # Предметы, которые уже заняты на этом уроке

        for grade in range(length[0], length[1]):
            available_subjects = [
                subj for subj in schedule[grade]
                if subj not in used_subjects and schedule[grade][subj]["remaining"] > 0
            ]

            if available_subjects:
                chosen_subject = random.choice(available_subjects)
                cabinet = schedule[grade][chosen_subject]["cabinet"]
                cell_content = f"{chosen_subject} {cabinet}"
                daily_schedule[grade][lesson_index] = f"{cell_content:<{cell_width}}"
                used_subjects.add(chosen_subject)
                schedule[grade][chosen_subject]["remaining"] -= 1  # Уменьшаем оставшееся количество уроков

    # Формируем таблицу
    table = []

    # Заголовок с номерами классов
    header = ["|"]
    for grade in range(length[0], length[1]):
        header.append(f"{str(grade)+' класс':^{cell_width}}|")
    table.append(header)

    # Заполняем строки с уроками
    for lesson_index in range(6):
        row = ["|"]
        for grade in range(length[0], length[1]):
            cell = daily_schedule[grade][lesson_index]
            if cell == '':
                cell = ' ' * cell_width  # Пустая ячейка должна быть такой же длины
            row.append(f"{cell}|")
        table.append(row)

    # Вывод таблицы
    separator = f"+{'-'*((cell_width+1) * (length[1]-length[0])-1)}+"  # Корректная длина разделителя
    print(separator)
    for row in table:
        print("".join(row))
        print(separator)

# Генерация расписания на день
generate_schedule(cell_width=18, length=[5, 12])
