class GameStats:
    " " "Track statistics for Robot Game." " "

    def __init__(self, robot_game):
        " " "Initialize statistics" " "
        self.settings = robot_game.settings
        self.reset_stats()

        # Start Robot Game in an active state.
        self.game_active = False

        # High score should never be reset.
        self.high_score = 0


    def reset_stats(self):
        " " "Initialize statistics that can change during the game." " "
        self.robots_left = self.settings.robot_limit
        self.score = 0
        self.level = 1
        


