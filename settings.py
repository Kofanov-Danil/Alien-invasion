import pygame
class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""
    
    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)

        # Настройки корабля
        self.size_of_ship = 3.5
        self.ship_speed = 3
        self.size_of_smoke = 3.5

        # Параметры снаряда
        self.bullet_speed = 2
        self.bullet_width = 5
        self.bullet_height = 25
        self.bullet_color = (60, 60, 60)
        # Ограничение количества снаряда
        self.bullets_allowed = 3


