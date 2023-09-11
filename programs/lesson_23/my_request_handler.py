import http.server
import random
import sqlite3


# Создаем свой класс
class MyHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    # Свой метод обработки GET запросов
    def do_GET(self):
        # Отправляем заголовки

        # Код статуса
        self.send_response(200)
        # Указываем, какого типа инфа будет отправляться в ответ
        self.send_header("Content type", "text/html")
        # Завершаем описание заголовок
        self.end_headers()
        # Данные для ответа записываем методом write переменной wfile
        # self.wfile.write('''<!DOCTYPE html>
        #                     <html lang="en">
        #                     <head>
        #                         <meta charset="UTF-8">
        #                         <meta name="viewport" content="width=device-width, initial-scale=1.0">
        #                         <title>Document</title>
        #                     </head>
        #                     <body>
        #                         <h1 style="color: aqua;">Сайт загружен</h1>
        #                     </body>
        #                     </html>'''.encode('UTF-8'))
        self.wfile.write(f'{random.randint(0, 3)}'.encode('UTF-8'))
    # Свой метод обработки GET запросов
    def do_POST(self):
        # Отправляем заголовки

        # Код статуса
        self.send_response(200)
        # Указываем, какого типа инфа будет отправляться в ответ
        self.send_header("Content type", "text/html")
        # Завершаем описание заголовок
        self.end_headers()
        # Можем сразу ответить
        # self.wfile.write("Post-запрос получен".encode('UTF-8'))

        # При считывании необходимо указать сколько данных мы считываем
        content_len = int(self.headers["Content-Length"])
        # Считаем даннык и сразу декодируем из бинарной формы
        response = self.rfile.read(content_len).decode()
        print(response)


        result = {}
        # Обработаем получаемую строку
        for pair in response.split('&'):
            date_key, data_value = pair.split('=')
            result[date_key] = data_value


        query = 'INSERT INTO users(name, age) VALUES(?, ?)'
        query_data = (result['name'], result['age'])
        cursor.execute(query, query_data)
        con.commit()

        self.wfile.write("Post-запрос получен".encode('UTF-8'))


def run(server_class=http.server.HTTPServer, handler_class=MyHTTPRequestHandler):
    server_adress = ('', 8000)
    httpd = server_class(server_adress, handler_class)
    httpd.serve_forever()


con = sqlite3.connect('lesson_23/my_db.db')
cursor = con.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100),
    age VARCHAR(100)
);
''')

run()


con.commit()
cursor.close()
con.close()







