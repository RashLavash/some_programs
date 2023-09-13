# Создаем свой тип исключения

class BirthYearError(Exception):
    def __str__(self):
        return 'Введен невозможный год рождения'


try:
    year = int(input('Введите ваш год рождения: '))
    if year < 1900 or year > 2023:
        # Мы сами поднимаем исключение при определенном условии
        raise BirthYearError
    print(f'Значение {year} пинято, вы зарегистрированы')
except ValueError:
    print('Введите значение соответствующего типа.')
except BirthYearError as error:
    print('Error', error)
except Exception as error:
    print('Error: ', error)

num1 = int(input())
num2 = int(input())

if num2 == 0:
    print('У вас ошибка - на ноль днлить нельзя')
else:
    print(num1 / num2)
try:
    print(num1 / num2)
except Exception as error:
    print('Error:', error)
