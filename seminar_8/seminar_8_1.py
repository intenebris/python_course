# import sqlite3 as sl
# from easygui import *

# conn = sl.connect("study.db")

# cur = conn.cursor()

# cur.execute("""
#             CREATE TABLE IF NOT EXISTS students
#             (id INTEGER PRIMARY KEY,
#             name TEXT,
#             surname TEXT
#             );""")

# # cur.execute("INSERT INTO students VALUES (1, 'Ваня', 'Петров')")
# # cur.execute("INSERT INTO students VALUES (2, 'Сергей', 'Сергеев')")
# # cur.execute("INSERT INTO students VALUES (3, 'Егор', 'Горбунков')")

# cur.execute("SELECT * FROM students;")
# res = cur.fetchall()
# print(res[len(res) - 1])

# conn.commit()
# conn.close()

import sqlite3 as sl
from easygui import *


def select_all():
    cur.execute("SELECT * FROM students;")
    return cur.fetchall()

def add_values():
    cur.execute("INSERT INTO students VALUES (1,'Ваня','Петров');")
    cur.execute("INSERT INTO students VALUES (2,'Сергей','Сергеев');")

def select_ivan():
    cur.execute("SELECT * FROM students WHERE name = 'Ваня';")
    return cur.fetchall()



conn = sl.connect("study.db")
cur = conn.cursor()
cur.execute("""
            CREATE TABLE IF NOT EXISTS students
            (id INTEGER PRIMARY KEY,
            name TEXT,
            surname TEXT
            );""")

choice = choicebox("Выберите запрос", "Главная форма",
                    ['Все записи', "Только Ваня"])


if choice == "Все записи":
    msg = select_all()
    msgbox(msg, "Результат запроса")


elif choice == "Только Ваня":
    msg = select_ivan()
    msgbox(msg, "Результат запроса")


conn.commit()
conn.close()