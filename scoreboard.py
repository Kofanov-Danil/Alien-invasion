import pygame.font
from pygame.sprite import Group
from healf import Healf
import json

from ship import Ship


class Scoreboard():
    """Класс для вывода игровой информации."""

    def __init__(self, ai_game):
        """Инициализирует атрибуты подсчета очков."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Настройки шрифта для вывода счета.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        # # Подготовка изображений счетов.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_healfs()

    def prep_healfs(self):
        """Сообщает количество оставшихся кораблей."""
        self.healfs = Group()
        for healf_number in range(self.stats.ships_left):
            healf = Healf(self.ai_game)
            healf.rect.x = 10 + healf_number * healf.rect.width * 1.2
            healf.rect.y = 20
            self.healfs.add(healf)

    def prep_level(self):
        """Преобразует уровень в графическое изображение."""
        level_str = f'level {str(self.stats.level)}'
        self.level_image = self.font.render(level_str, True,
                                          self.text_color, self.settings.bg_color)

        # Уровень выводится под текущим счетом.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_score(self):
        """Преобразует текущий счет в графическое изображение."""

        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str,
                                            True,self.text_color, self.settings.bg_color)

        # Вывод счета в правой верхней части экрана.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 10

    def show_score(self):
        """Выводит очки, уровень и количество кораблей на экран."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.healfs.draw(self.screen)

    def prep_high_score(self):
        """Преобразует рекордный счет в графическое изображение."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                                           self.text_color, self.settings.bg_color)

        # Рекорд выравнивается по центру верхней стороны.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        """Проверяет, появился ли новый рекорд."""
        if self.stats.score > self.stats.high_score:
            filename = 'save.json'
            with open(filename, 'w') as save:
                json.dump(self.stats.score, save)
            self.stats.high_score = self.stats.score
            self.prep_high_score()



