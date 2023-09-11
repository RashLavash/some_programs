import sqlite3


user_chek = int(input('Добавить новый фильм? Если да, введите 1, если нет, Введите 0 : \n'))


connect = sqlite3.connect('lesson_18/user_films.db')
cursor = connect.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS films(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    film_title VARCHAR(100),
    film_author VARCHAR(100),
    film_year INTEGER
);
''')


while user_chek == 1:
    film_title = input('Введите название фильма : ')
    film_author = input('Введите автора фильма : ')
    film_year = input('Введите год выпуска фильма : ')

    query_data = (film_title, film_author, film_year)
    query = ''' INSERT INTO films(film_title, film_author, film_year) VALUES(?, ?, ?)'''
    cursor.execute(query, query_data)

    connect.commit()


    user_chek = int(input('Добавить новый фильм? Если да, введите 1, если нет, Введите 0 : \n'))

    if user_chek == 0:
        break
    else:
        user_chek = input('Введите либо 1, если да, либо 0, если нет: ')

cursor.close()   
connect.close()   


