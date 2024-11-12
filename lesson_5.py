import sqlite3

connect = sqlite3.connect("students.db")
cursor = connect.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS grades (
    student_id INTEGER,
    subject TEXT,
    grade INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(id)
)
''')

def add_student(name, age):
    cursor.execute('''
    INSERT INTO students (name, age) VALUES (?, ?)
    ''', (name, age))
    connect.commit()

def add_grade(student_id, subject, grade):
    cursor.execute('''
    INSERT INTO grades (student_id, subject, grade) VALUES (?, ?, ?)
    ''', (student_id, subject, grade))
    connect.commit()

def get_student_grades(student_id):
    cursor.execute('''
    SELECT subject, grade FROM grades WHERE student_id = ?
    ''', (student_id,))
    grades = cursor.fetchall()
    for subject, grade in grades:
        print(f'{subject}: {grade}')

def average_grade(student_id):
    cursor.execute('''
    SELECT AVG(grade) FROM grades WHERE student_id = ?
    ''', (student_id,))
    avg_grade = cursor.fetchone()[0]
    return avg_grade


add_student('Леха', 15)
add_student('Саня', 15)

add_grade(1, 'Математика', 5)
add_grade(1, 'Физика', 4)
add_grade(2, 'Математика', 3)
add_grade(2, 'История', 5)

print("Оценки Лехи:")
get_student_grades(1)
print("Средний балл Лехи:", average_grade(1))

print("\nОценки Сани:")
get_student_grades(2)
print("Средний балл Сани:", average_grade(2))

connect.close()