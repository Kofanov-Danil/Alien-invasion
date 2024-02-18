import pygame

class Musics():
    """"Класс для управления звуками игры"""

    def __init__(self, ai_game):
        self.settings = ai_game.settings

    def _background_music(self):
        """Добавление фоновой музыки"""
        pygame.mixer.music.load("musics/background_music.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.05)

    def sound_of_a_gunshot(self):
        """Добавление звука выстрела"""
        gunshot = pygame.mixer.Sound("musics/sound_of_a_gunshot.ogg")
        gunshot.set_volume(0.1)
        gunshot.play()

    def hitting_the_alien(self):
        """Добавление звука попадания снаряда в пришельца"""
        hit = pygame.mixer.Sound("musics/sound_of_hit.ogg ")
        hit.set_volume(0.1)
        hit.play()

    def sound_of_new_level(self):
        """Добавление звука перехода на новый уровень"""
        new_level = pygame.mixer.Sound("musics/sound_of_new_level.ogg")
        new_level.set_volume(0.3)
        new_level.play()

    def sound_of_new_game(self):
        """Добавление звука начала новой игры"""
        new_game = pygame.mixer.Sound("musics/sound_of_new_game.ogg")
        new_game.set_volume(0.3)
        new_game.play()

    def sound_of_game_over(self):
        """Добавление звука проигрыша"""
        game_over = pygame.mixer.Sound("musics/sound_of_game_over.ogg")
        game_over.set_volume(0.1)
        game_over.play()
