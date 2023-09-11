class Organism:
    def __init__(self, org):
        self.org = org
        if self.org.lower() == 'человек':    
            self.__hands = 2
            self.__legs = 2
        else:
            pass

    def walking(self):
        print('Вы ходите')

    def breathing(self):
        print('Вы дышите')

    @property
    def human_password(self):
        password = input('Введите пароль :\n')
        if password == 'hands':
            return self.__hands
        elif password == 'legs':
            return self.__legs
        else:
            print('В доступе отказано!')

class Animals(Organism):
    def __init__(self, org):
        super().__init__(org)
        self.__legs = 4

    @property
    def animal_password(self):
        password = input('Введите пароль :\n')
        if password == 'legs':
            return self.__legs
        else:
            print('В доступе отказано!')

human = Organism('человек')
dog = Animals('soba4ka')
dog.breathing()
# print(human.human_password)
# print(dog.animal_password)
