import pygame
class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""
    
    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)

        # Размер корабля
        self.size_of_ship = 3.5

