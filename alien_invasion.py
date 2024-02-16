import sys

import pygame

from settings import Settings
from ship import Ship
from ship_smoke import ShipSmoke
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()
        self.settings = Settings()

        # Режим FULLSCREEN:
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.ship_smoke = ShipSmoke(self)
        self.bullets = pygame.sprite.Group()

        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            self._check_events()
            self.ship.update()
            self.ship_smoke.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()

    def _update_bullets(self):
        """Обновляет позиции снарядов и уничтожает старые снаряды."""
        # Обновление позиций снарядов.
        self.bullets.update()

        if not self.aliens:
            # Уничтожение существующих снарядов и создание нового флота.
            self.bullets.empty()
            self._create_fleet()



        # Удаление снарядов, вышедших за край экрана.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        # Проверка попаданий в пришельцев.
        # При обнаружении попадания удалить снаряд и пришельца.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

    def _check_events(self):
            """Отслеживание событий клавиатуры и мыши."""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Реагирует на нажатие клавиш."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
            self.ship_smoke.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
            self.ship_smoke.moving_left = True
        # Выход на кнопку 'q'
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Реагирует на отпускание клавиш."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
            self.ship_smoke.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
            self.ship_smoke.moving_left = False

    def _fire_bullet(self):
        """Создание нового снаряда и включение его в группу bullets."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        #Выпускание дыма при нажатии клавиши
        if self.ship_smoke.moving_right or self.ship_smoke.moving_left:
            self.ship_smoke.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        # Отображение последнего прорисованного экрана.
        pygame.display.flip()

    def _create_fleet(self):
        """Создание флота вторжения."""
        # Создание пришельца и вычисление количества пришельцев в ряду
        # Интервал между соседними пришельцами равен ширине пришельца.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        # определяет количество рядов, помещающихся на экране
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                               (2 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Создание флота вторжения.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Создание пришельца и размещение его в ряду."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_aliens(self):
        """
        Проверяет, достиг ли флот края экрана,
        с последующим обновлением позиций всех пришельцев во флоте.
        """
        self._check_fleet_edges()
        self.aliens.update()

    def _change_fleet_direction(self):
        """Опускает весь флот и меняет направление флота."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_fleet_edges(self):
        """Реагирует на достижение пришельцем края экрана."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()
