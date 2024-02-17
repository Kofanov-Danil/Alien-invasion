import json
class GameStats():
    """Отслеживание статистики для игры Alien Invasion."""
    def __init__(self, ai_game):
        """Инициализирует статистику."""
        self.settings = ai_game.settings
        self.reset_stats()
        # Рекорд не должен сбрасываться.

        filename = 'save.json'
        with open(filename, "r", encoding="UTF-8") as save:
            self.high_score = int(json.load(save))


        # Игра запускается в неактивном состоянии.
        self.game_active = False




    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1