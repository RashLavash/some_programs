# python --version
#
# pip freeze > requirements.txt
# pip uninstall - удаление библиотеки
# pyinstaller --onefile first.py

# Смена линтера CTRL + SHIFT + P, пишем Select Linter, выбираем mypy

# Аннотация типов

# <имя переменной>: <тип переменной> = <присваивание значений>
name: str = 'Rashid'
print(name)


# def <имя функции>(<аргумент1: (тип аргумента)>, <аргумент2: (тип аргумента)>) -> (тип аргумента)
def my_sum(num1: int, num2: int) -> int:
    return num1 + num2 
    
print(my_sum(1, 5))





