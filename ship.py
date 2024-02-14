import pygame
from settings import Settings
class Ship():
    """"Класс для управления кораблём"""
    def __init__(self, ai_game):
        """Инициализирует корабль и задает его начальную позицию."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = Settings()

        #Загружает изображение корабля и задает его размер и начальную позицию
        self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // self.settings.size_of_ship,
               self.image.get_height() // self.settings.size_of_ship))
        self.rect = self.image.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)

