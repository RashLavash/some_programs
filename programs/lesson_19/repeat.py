import sqlite3


con = sqlite3.connect('lesson_19/first_db.db')
cursor = con.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(200),
    author VARCHAR(60),
    year INTEGER(5)               
);
''')

# cursor.execute('''
# INSERT INTO books VALUES(
#     'Маленький принц',
#     'Антуан Экзюпери',
#     1942
# );
# ''')

query = ''' INSERT INTO books(title, author, year) VALUES(?, ?, ?) '''
query_data = ('Маленький принц', 'Антуан Экзюпери', 1942)
cursor.execute(query, query_data)


con.commit()
cursor.close()
con.close()





