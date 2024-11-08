""" База Данных """
""" Система Управления Базой Данных """
""" CRUD - Create, Retrive, Update, Delete """

import sqlite3

connect = sqlite3.connect("itpark.db")
cursor = connect.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS itpark(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name VARCHAR (30) NOT NULL,
        age INT DEFAULT NULL,
        direction TEXT,
        is_have BOOLEAN NOT NULL DEFAULT FALSE,
        rating DOUBLE (4,2) DEFAULT (0.0),
        birth_date DATE
    )
""")

def register():
    full_name = input("Введите ФИО: ")
    age = int(input("Введите свой возраст: "))
    direction = input("Введите направление: ")
    is_have = bool(input("Наличие ноутбука: "))
    rating = float(input("Введите свой рейтинг: "))
    birth_date = input("Введите дату рождения: ")

    # cursor.execute(f""" INSERT INTO itpark 
    #                (full_name, age, direction, is_have, rating, birth_date)
    #                VALUES ('{full_name}', {age}, '{direction}', {is_have}, {rating}, '{birth_date}')""")
    # connect.commit()
    
    cursor.execute(f""" INSERT INTO itpark 
                   (full_name, age, direction, is_have, rating, birth_date)
                   VALUES (?, ?, ?, ?, ?, ?)""", (full_name, age, direction, is_have, rating, birth_date))
    connect.commit()

def delete_students(id):
    cursor.execute(""" DELETE FROM itpark WHERE id = ?""", (id,))
    # students = cursor.fetchone()
    # print(students)
    connect.commit()

def all_students(id):
    cursor.execute(""" SELECT * FROM itpark WHERE id = ? """, (id,))
    students = cursor.fetchone()
    print(students)

all_students(1)