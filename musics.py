import pygame

class Musics():

    def __init__(self, ai_game):
        self.settings = ai_game.settings

    def _background_music(self):
        pygame.mixer.music.load("musics/background_music.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.05)