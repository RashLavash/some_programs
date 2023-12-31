import sqlite3

con = sqlite3.connect('lesson_21/my_db.db')
cursor = con.cursor()



cursor.execute('''
CREATE TABLE IF NOT EXISTS directors(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(60)           
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS films(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100),
    director INTEGER,
    year INTEGER(5),
    FOREIGN KEY(director) REFERENCES directors(id)
);
''')

dir_query = '''
INSERT INTO directors(name) VALUES(?)
'''
dir_query_data = [
    ('Роберт Земекис',),
    ('Зак снайдер',)
]
# cursor.executemany(dir_query, dir_query_data)


query = '''
INSERT INTO films(title, director, year) VALUES(?, ?, ?)
'''
query_data = [
    ('Форест Гамп', 1, 1986),
    ('300', 2, 2004),
    ('Хранители', 2, 2007)
]

# cursor.executemany(query, query_data)


cursor.execute('''
SELECT title, year 
FROM films
''')
# print(cursor.fetchall())

cursor.execute('''
SELECT films.title, directors.name
FROM films
JOIN directors ON films.director = directors.id
''')

print(cursor.fetchall())

con.commit()
cursor.close()
con.close()