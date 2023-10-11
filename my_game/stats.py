class Stats():
    """отслеживание статистики"""
    def __init__(self):
        """инициализируем статистику"""
        self.reset_stats()
        self.run_game = True
        with open('my_game/high_score.txt', 'r') as file:
            self.high_score = int(file.readline())

    
    def reset_stats(self):
         """статистика изменяющаяся во время игры"""
         self.guns_left = 3
         self.score = 0
