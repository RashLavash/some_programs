# try:
#     print(1 / 0)
#     int('Hello')
#     print(1 / 0)

# except ValueError as error:
#     print('Типовая ошибка: ', error)
# except ZeroDivisionError as error:
#     print('На ноль делить нельзя: ', error)

# s = 'zdrasty'

# try:
#     s[9]
# except ValueError as error:
#     print('Ошибка с типом данных : ', error)
# except IndexError as error:
#     print('Ошибка индекса: ', error)

# d = {}
# try:
#     d['key']
# except KeyError as error:
#     print('Ошибка ключа: ', error)
# except LookupError as error:
#     print('Ошибка индекса: ', error)
# finally:
#     print('end')

try:
    1 / 0

except (KeyError, IndexError) as error:
    print('Ошибка: ', error)
except ZeroDivisionError as error:
    print('На 0 делить нельзя: ', error)

else:
    print('')
finally:
    print('end')

