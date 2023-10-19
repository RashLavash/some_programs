from flask import Flask

app = Flask(__name__) # Создаем экземпляр класса Flask

@app.route('/new_page') # rout - обработчик запроса. По получаемому URL, т.е. ('/')
                        # По запрошенному URL, т.е. ('/new_page'), обрабатывает запрос
@app.route('/')
def new_page():         # После принятия запроса, создаем выполняемую функцию для этого запроса
    return "new_page"

@app.route('/about')
def new_page_2():
    return "<h1>About us</h1>"


if __name__ == '__main__': # Если этот файл запускается не импортировано, то он запустится,
    app.run(debug=True)    # А если запустится импортом из другого файла, то второй раз программа не запустится