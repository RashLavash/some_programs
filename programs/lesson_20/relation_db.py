import sqlite3


con = sqlite3.connect('lesson_20/second.db')
cursor = con.cursor()

cursor.execute(''' DROP TABLE books ''')
cursor.execute(''' DROP TABLE authors  ''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(255),
    author_id INTEGER,
    year INTEGER(5),
    FOREIGN KEY(author_id) REFERENCES authors(id)
);
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS authors(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(60)           
);
''')
author_query = '''
INSERT INTO authors(name) VALUES(?)
'''
author_data = [
    ('Лев Толстой',),
    ('Пушкин А.С.',),
    ('Берроуз',)
]
cursor.executemany(author_query, author_data)


book_query = '''
INSERT INTO books(title, author_id, year) VALUES(?, ?, ?)
'''
query_data = [
    ('Война и мир', 1, 1950),
    ('Джанки', 3, 1997),
    ('Анна Каренина', 2, 1877)
]
cursor.executemany(book_query, query_data)

cursor.execute('''
SELECT books.title, authors.name
FROM books, authors
WHERE books.author_id = authors.id
''')


print(cursor.fetchall())

con.commit()
cursor.close()
con.close()





