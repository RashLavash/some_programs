import sqlite3

con = sqlite3.connect('lesson_19/another.db')
cursor = con.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS films(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100),
    author VARCHAR(60),
    year INTEGER(5)
);
''')

query = '''
INSERT INTO films(title, author, year) VALUES(?, ?, ?)
'''
film_list = [
    ('Мотылек', 'Михаэль Ноера', 2017),
    ('Джентельмены', 'Гая Ричи', 2020),
    ('INTERSTELLAR', 'Кристофер Нолан', 2014),
    ('Кингсман: Золлотое кольцо', 'Мэттью Вон', 2017),
    ('Мачо и ботан', 'Фил Лорд и Кристофер Миллер', 2012),
    ('Эскобар', 'Фернандо Леона де Араноа', 2017),
    ('Гранд Торино', 'Клинт Иствуд', 2008),
    ('Все везде и сразу', 'Дэниела Шайнерт и Ден Кван', 2022)
]

# cursor.executemany(query, film_list)
# cursor.execute('''
# SELECT * FROM films
# ''')

# cursor.execute('''
# SELECT title
# FROM films
# WHERE title LIKE '%Торино'
# ''')

# Упорядочиваем бд по возрастанию годов от 2017 до 2022
# ORDER BY (название поля) - упорядочивает по возростанию,
# добавив DESC - по убыванию, 
# а добавив LIMIT (количествов) вернет указанное количество упорядоченных элементов

# cursor.execute('''
# SELECT year, title 
# FROM films
# WHERE year BETWEEN 2017 AND 2022 ORDER BY year DESC LIMIT 3
# ''')

cursor.execute('''
UPDATE films
SET author = 'М. Вон'
WHERE author == 'Мэттью Вон'
''')

cursor.execute('''
DELETE FROM films
WHERE author = 'М. Вон'
''')

cursor.execute('''
SELECT * FROM films
''')
print(cursor.fetchall())


con.commit()
cursor.close()
con.close()