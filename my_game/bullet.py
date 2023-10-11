import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, mega_gun):
        """создание пули в текущийпозиции пушки"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 50, 12)
        self.color = 139, 195, 74
        self.speed = 4.5
        self.rect.centerx = mega_gun.rect.centerx
        self.rect.top = mega_gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """перемещение пули вверх"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """рисуем пулю на экране"""
        pygame.draw.rect(self.screen, self.color, self.rect)