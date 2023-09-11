# ООП - объектно - ориентированное програмирование
# Классы и объекты


# def srart_car(car):
#     car1['gazoline1'] -= car1['spend']
#     car1['motor1'] = True




# car1 = {
#     'speed1': 0, 
#     'gazoline1': 20, 
#     'motor1': False,
#     'color': 'white',
#     'spend': 3
# }

# car2 = {
#     'speed1': 0, 
#     'gazoline1': 20, 
#     'motor1': False,
#     'color': 'red'
# }

# Реализация через ООП
class Car:
    speed = 0
    gazoline = 20
    motor = False
    color = 'white'
    spend = 3

    def srart_car(self):
        self.speed = 50
        self.motor = True
        self.gazoline -= self.spend
    
    def gazolin_info(self):
        print(f'В баке осталось {self.gazoline} топлива')

car1 = Car() # Создаем экземпляр класса Car
car1.gazolin_info()
car1.srart_car()
car1.gazolin_info()
print(car1.gazoline)