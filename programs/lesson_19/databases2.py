# Рассматрвиаем считывание данных из таблицы

import sqlite3


con = sqlite3.connect('lesson_19/second_db.db')
cursor = con.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY AUTOINKREMENT,
    title VARCHAR(200),
    author VARCHAR(60),
    year INTEGER(5)               
);
''')

# Добавим 5 записей в таблицу через команду executemany

query = ''' 
INSERT INTO books(title, author, year) VALUES(?, ?, ?) 
'''

books_list = [
    ('Властелин колец', 'Джон Толкин', 1949),
    ('Зеленая миля', 'Стивен Кинг', 1996),
    ('Финансист', 'Теодор Драйзер', 1912),
    ('Титан', 'Теодор Драйзер', 1914),
    ('Стоик', 'Теодор Драйзер', 1945)
]
# cursor.executemany(query, books_list)

# Считывание данных

cursor.execute('''
SELECT * FROM books
''')
cursor.execute('''
SELECT title FROM books
''')
cursor.execute('''
SELECT title, year FROM books
''')

cursor.execute('''
SELECT title, year
FROM books
WHERE year < 1940               


''')

cursor.execute('''
SELECT title, year
FROM books
WHERE year = 1945               


''')

cursor.execute('''
SELECT title, year
FROM books
WHERE year > 1930 AND year < 1950 ORDER BY year DESC LIMIT 1               

''')

cursor.execute('''
SELECT title, year
FROM books
WHERE year BETWEEN 1930 AND 1950 ORDER BY year DESC LIMIT 1

''')

cursor.execute('''
SELECT title, year
FROM books
WHERE author IN ('Чак Паланик', 'Теодор Драйзер', 'Виктор Пелевин')

''')

# Шаблон команды LIKE принимает строки с % (от 0 до беск - ти символов)
# и _ (нижнего подчеркивания, 1 подчеркивание = 1 символ)
cursor.execute('''
SELECT title, year
FROM books
WHERE title LIKE '%ы'

''')

# По курсору можно пройтись как по итератору циклом
# for row in cursor:
#     print(row)

# Команда fetchall() возвращает данные из списка

# result = cursor.fetchall()
# print(result)

# cursor.execute('''
# SELECT author FROM books
# ''')

# Можно вызывать функции для группы данных
# а именно : MIN, MAX, AVG, SUM, COUNT
cursor.execute('''
SELECT author, COUNT(year)
FROM books
GROUP BY author
''')
print(cursor.fetchall())

# Изменение данных
cursor.execute('''
UPDATE books
SET author = 'С. Кинг'
WHERE author == 'Стивен Кинг'
''')

# Удаление данных
cursor.execute('''
DELETE FROM books
WHERE author = 'С. Кинг'
''')
cursor.execute(''' SELECT * FROM books ''')
print(cursor.fetchall())

con.commit()
cursor.close()
con.close()





