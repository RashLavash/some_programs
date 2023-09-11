import sqlite3


con = sqlite3.connect('lesson_20/first.db')
cursor = con.cursor()



cursor.execute('''
CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY AUTOINKREMENT,
    title VARCHAR(255),
    author VARCHAR(60),
    year INTEGER(5)
);
''')
query = '''
INSERT INTO books(title, author, year) VALUES(?, ?, ?)
'''
query_data = ('Война и мир', 'Лев Толстой', 1850)
cursor.execute(query, query_data)

cursor.execute('''
UPDATE books
SET year = 1869
''')

cursor.execute('''
DELETE FROM books
WHERE title = 'Война и мир'
''')

cursor.execute('''
SELECT * FROM books
''')
print(cursor.fetchall())