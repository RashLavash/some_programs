# Исключения

# Структура try..except
# try:
#     <код, который может вызвать исключения>
# except <уласс исклюяения 1>:
#     <код обработки исключения>
# except <уласс исклюяения 1>:
#     <код обработки исключения>
# except <уласс исклюяения 1>:
#     <код обработки исключения>
# except <уласс исклюяения 1>:
#     <код обработки исключения>
# else:
#     <если не было исключений, код выполнится>
# finally:
#    <код, выполняющийся всегда>


# Конструкция  try..except
try:
    num1 = int(input())
    num2 = int(input())
    print(f'{num1} / {num2} = {num1 / num2}')

# Ловим исключение типа ZeroDivisionError
except ZeroDivisionError:
    print('На 0 делить нельзя')
# Ловим исключение типа ZeroDivisionError
except ValueError:
    print('Было введено неподходящее значение')
# Ловим остальные ошибки родительским классом Exception
except Exception as error:
    print('Ошибка:', error)

else:
    print('Без ошибок')

finally:
    ('Код выполнился без ошибок')


print('Программа завершена')



