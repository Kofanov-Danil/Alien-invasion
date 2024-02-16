import pygame
class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""
    
    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1280
        self.screen_height = 1024
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

        # Настройки пришельцев
        self.size_of_alien = 5
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1



