import pygame
from pygame.sprite import Group

from settings import Settings
from pygame.sprite import Sprite

class Healf(Sprite):
    """"Класс для иконки здороья"""

    def __init__(self, ai_game):
        """Инициализирует иконку здоровья начальную позицию."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Загружает изображение иконки, задает его размер и начальную позицию
        self.image = pygame.image.load('images/healf.bmp')
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // self.settings.size_of_healf,
                                                         self.image.get_height() // self.settings.size_of_healf))
        self.rect = self.image.get_rect()




