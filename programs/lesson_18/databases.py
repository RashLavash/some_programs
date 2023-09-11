import sqlite3

con = sqlite3.connect('lesson_18/films.db')
cursor = con.cursor()


# cursor.execute('''
# DROP TABLE films
# ''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS films(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(255),
    genre VARCHAR(255),
    year INTEGER             
);
''')


user_films = input('Введите название своего фильма : ')
user_genre = input('Введите жанр своего фильма : ')
user_year = int(input('Введите год выпуска своего фильма : '))

query_data = (user_films, user_genre, user_year)
query = '''
    INSERT INTO films(title, genre, year) VALUES(?, ?, ?)
'''
cursor.execute(query, query_data)


con.commit()
cursor.close()
con.close()