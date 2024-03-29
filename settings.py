import pygame
class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""
    
    def __init__(self):
        """Инициализирует статические настройки игры."""
        # Параметры экрана
        self.screen_width = 1280
        self.screen_height = 1024
        self.bg_color = (255, 255, 255)

        # Настройки корабля
        self.size_of_ship = 3.5
        #self.ship_speed = 3
        self.size_of_smoke = 3.5
        self.ship_limit = 3

        # Параметры снаряда
        #self.bullet_speed = 2
        self.bullet_width = 5
        self.bullet_height = 25
        self.bullet_color = (60, 60, 60)
        # Ограничение количества снаряда
        self.bullets_allowed = 4

        # Настройки пришельцев
        self.size_of_alien = 7
        #self.alien_speed = 1
        self.fleet_drop_speed = 30


        # Темп ускорения игры
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

        # Темп роста стоимости пришельцев
        self.score_scale = 1.5

        # Настройки иконки здоровья
        self.size_of_healf = 7.5

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        self.ship_speed = 1.5
        self.bullet_speed = 2.0
        self.alien_speed = 1.0

        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1

        # Подсчет очков
        self.alien_points = 50

    def increase_speed(self):
        """Увеличивает настройки скорости и стоимости пришельцев"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)



