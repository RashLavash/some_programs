# import requests


# api_server = 'https://youtube.com/results'
# api_params = {
#     'search_query': 'bmw m3 e46'
# }
# response = requests.get(api_server, params=api_params)
# print(response.status_code)
# print(response.url)


# class Animals:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#         self.paws = 4

#     def animsl_sound(self):
#         print('Издает звук')

# class Cat(Animals):
#     def animsl_sound(self):
#         # super().animsl_sound()
#         print('Мияу')
# class Dog(Animals):
#     def __init__(self, name, color, ancenstry):
#         super().__init__(name, color)
#         self.ancenstry = ancenstry
    
#     def animsl_sound(self):
#         print('Гав гав!')

#     def bite(self):
#         print('Кусает')
    


# doger = Dog('Съебастьян', 'белый', 'чистокровный')
# print(doger.ancenstry)
# doger.bite()

# print()

# cat = Cat('Барбарис', 'серый')
# cat.animsl_sound()


class MyError(Exception):
    def __str__(self):
        return 'Моя ошибка'

try:
    user_input = int(input())
    if user_input < 50 or user_input > 100:
        raise MyError
    else:
        print('Нормально все')
except ValueError as error:
    print('Типовая ошибка', error)
except MyError as error:
    print('А когда не ошибка', error)
finally:
    print('vse uzhe')

# try:
#     num = int(input('Введите число'))
#     print(num)
# except ValueError as error:
#     print('Вы ввели не число!', error)

