import pygame
import ship
from settings import Settings
class ShipSmoke():
    """"Класс для управления дымом корабля"""
    def __init__(self, ai_game):
        """Инициализирует дым корабля и задает его начальную позицию."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Загружает изображение корабля и задает его размер и начальную позицию
        self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // self.settings.size_of_ship,
                                                         self.image.get_height() // self.settings.size_of_ship))
        self.rect = self.image.get_rect()

        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

        ##Загружает изображение дыма корабля и задает его размер и начальную позицию
        self.image_smoke = pygame.image.load('images/rocket smoke.bmp')
        self.image_smoke = pygame.transform.scale(self.image_smoke,
                                                  (self.image_smoke.get_width() // self.settings.size_of_smoke,self.image_smoke.get_height() // self.settings.size_of_smoke))
        self.rect_smoke = self.image_smoke.get_rect()
        self.rect_smoke.midbottom = self.screen_rect.midbottom
        self.xx = float(self.rect_smoke.x)

        #Флаг перемещения
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """Обновляет позицию корабля и дыма с учетом флага."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.xx += self.settings.ship_speed
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.xx -= self.settings.ship_speed
            self.x -= self.settings.ship_speed

        # Обновление атрибута rect на основании self.x.
        self.rect_smoke.x = self.xx
        self.rect.x = self.x

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image_smoke, self.rect_smoke)

