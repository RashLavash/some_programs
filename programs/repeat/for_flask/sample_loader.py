# Загрузчики шаблонов
from jinja2 import Environment, FileSystemLoader, FunctionLoader


persons = [
    {'name': 'Алексей', 'old': 18, 'weight': 78.5},
    {'name': 'Иван', 'old': 28, 'weight': 82.3},
    {'name': 'Николай', 'old': 33, 'weight': 94.0}
]
# Импользуем загрузчик FileSystemLoader

# file_loader = FileSystemLoader('programs/repeat/for_flask/templates') # указываем путь до папки, в которой хранятся наши шаблоны
# env = Environment(loader=file_loader) # Environment - класс, отвечающий за работу API данного пакета
                                      # через именованный аргумент, передаем ему ссылку, хранящей нужные нам шаблоны

# tm = env.get_template('for_s_l.html') # формирует экземпляр класса, на основе содержимого выбранного файла
# message = tm.render(users=persons)
# print(message)

# Импользуем загрузчик FunctionLoader
def load_tpl(path):
    if path == "index":
        return '''Имя {{ user.name }}, возраст {{ user.old }}'''
    else:
        return '''Данные {{ user }}'''

file_loader = FunctionLoader(load_tpl) # передаем функцию, содержащую шаблоны
env = Environment(loader=file_loader) # Создам окружение для работы с нашими шаблонами

tm = env.get_template('index')
message = tm.render(user=persons[0]) # формируем экземпляр класса, на основе содержимого выбранного файла

print(message)