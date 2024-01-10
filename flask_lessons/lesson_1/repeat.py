def info(func):
    def wrapper():
        func()


    return wrapper

@info
def sum_1(num1, num2):
    return num1 + num2
