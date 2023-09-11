import sqlite3


connect = sqlite3.connect('lesson_18/new_films.db')
cursor = connect.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS films(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    film_title VARCHAR(100),
    film_autor VARCHAR(100),
    film_year INTEGER
);
''')


def query(film_title, film_autor, film_year):
    ''' Создаем запрос с помощью SQL  '''

    query_data = (film_title, film_autor, film_year)
    query = ''' INSERT INTO films(film_title, film_autor, film_year) VALUES(?, ?, ?) '''
    cursor.execute(query, query_data)

    connect.commit()

user_chek = input('Добавить новый фильм? Если да, введите 1, если нет, Введите 0 : \n')

if user_chek == '1':

    while user_chek == '1':
        user_input_film_title = input('Введите название фильма : ')
        user_input_film_autor = input('Введите название автора фильма : ')
        user_input_film_year = int(input('Введите год выпуска фильма (ввести нужно обязательно число) : '))

        query(user_input_film_title, user_input_film_autor, user_input_film_year)

        user_chek = input('Добавить новый фильм? Если да, введите 1, если нет, Введите 0 : \n')

        if user_chek == '0':
            break
        else:
            user_chek = input('Введите либо 1, если да, либо 0, если нет: ')
elif user_chek == '0':
    print('')
else:
    user_chek = input('Введите либо 1, если да, либо 0, если нет: ')

cursor.close()
connect.close()