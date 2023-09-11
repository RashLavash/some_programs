# Наследование

class Bank:
    def __init__(self, name, money):
        self.name = name
        self.__money = money

    @property
    def password(self):
        userpass = input('Введите парол!:\n')
        if userpass == '1588':
            return self.__money
        else:
            return 'Деньги не даам!'

    @password.setter
    def password(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            return 'Не дааам!'    


# user_1 = Bank('Rashidbeg', 98765)
# print(user_1.password)



# Полиморфизм


class Human:
    def run(self):
        print('Он ходит на двух ногах!')

class Animals:
    def run(self):
        print('Он бегит на четырех лапах!')
    
def run_or_run(obj):
    pass
    # obj.run()

# person = Human()
# gipard = Animals()
# lion = Animals()

# run_or_run(person)
# run_or_run(gipard)
# run_or_run(lion)

# Наследование

class Cars:
    def __init__(self, car_class, car_color):
        self.car_class = car_class.lower()
        self.car_color = car_color.lower()
        self.wheel = 4

    def start_car(self):
        print('Машина заводится с ключа')

    def speed_car(self):
        print('Максимальная скорость 100 км/ч')

class Pessenger_car(Cars):
    def start_car(self):
        print('Машина заводится нажатием на кнопку')

    def speed_car(self):
        print('Максимальная скорость 250 км/ч')

class Cargo_car(Cars):
    def __init__(self, car_class, car_color):
        super().__init__(car_class, car_color)
        self.cargo = True
        self.wheel = 10

    def start_car(self):
        super().start_car()

    def speed_car(self):
        print('Максимальная скорость 300 км/ч')


vaz_2107 = Cars('Легковая', 'вишневый')
Nissan = Pessenger_car('Легковая', 'темно-синяя')
Volvo_FH = Cargo_car('Грузовой', 'красный')

vaz_2107.start_car()
vaz_2107.speed_car()
print(vaz_2107.car_class)
print(vaz_2107.wheel)

print()

Nissan.start_car()
Nissan.speed_car()
print(Nissan.car_class)
print(Nissan.wheel)

print()

Volvo_FH.start_car()
Volvo_FH.speed_car()
print(Volvo_FH.car_class)
print(Volvo_FH.wheel)


