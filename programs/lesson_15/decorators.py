# Декораторы

# Структура декоратора:
# def <имя декоратора>(<имя пер-ой хранящей имходнуб фун-ю>)


# Декоратор 1

def add_mark(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + '.'
    return wrapper

# Декоратор 2

def func_info(func):
    def wrapper(*args, **kwargs):
        print(f'Название функции: {func.__name__}')
        print(f'Позиционные аргументы: {args}')
        print(f'Именованные аргументы: {kwargs}')
        result = func(*args, **kwargs)
        return result
    return wrapper
        
        

# Фун - я, которую расширили декоратором add_mark
@add_mark

def greeting(name):
    return f'Hello, {name}'

print(greeting('You'))

@func_info
def dialogue(name):
    return f'How are you, {name}'


print(greeting('Rashidbeg'))

new_greeting = func_info(greeting)
new_greeting('Заур')