class Car:
    # speed = 0
    # gazoline = 20
    # motor = False
    # color = 'white'
    # spend = 3

    def __init__(self, color, spend, gasoline):
        self.speed = 0
        self.gasoline = gasoline
        self.motor = False
        self.color = color
        self.spend = spend

    def srart_car(self):
        self.speed = 50
        self.motor = True
        self.gasoline -= self.spend
    
    def gazolin_info(self):
        print(f'В баке осталось {self.gasoline} топлива')

car1 = Car('white', 30, 5)
car2 = Car('white', 30, 5)
print(car1.color, car1.gasoline, car1.spend)