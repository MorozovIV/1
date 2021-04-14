import sqlite3 as sl
from sqlite3 import Connection

con: Connection = sl.connect('my-test.db')# создание базы данных

# with con:                                                   # подключение и создание таблицы user
#     con.execute("""
#         CREATE TABLE USER (
#             id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#             name TEXT,
#             age INTEGER
#         );
#     """)                                                    # создание 3 колонки id, name, age

sql = 'INSERT INTO USER (id, name, age) values(?, ?, ?)'      # запись данных в базу
data = [
(1, 'Alice', 21),
(2, 'Bob', 22),
(3, 'Chris', 23)
]                                                             # запись данных в базу
with con :
    con.executemany(sql, data)

with con:                                                     # вывод данных
    data = con.execute("SELECT * FROM USER WHERE age <= 22")
    for row in data:
        print(row)                                            # вывод данных