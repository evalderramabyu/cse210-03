class Parachute:
    
    def __init__(self):
        """
        Attributes
            _lives: integer
        """
        self._lives = 4
        ​
    def lose_life(self):
        """
        Takes a live away from the remaining lives of the game
        """
        self._lives -= 1
​
    def get_lifes(self):
        """
        Gets the remaining lives in the game.
        """
        return self._lives
​
    def draw_image(self, terminal_service):
        """Draws a picture of a parachute
        """
        method = '_level_' + str(self._lives)
        terminal_service.write_text(getattr(self, method)())
​
    def _level_4(self):
        """Draws a complete parachute to start the game
        """
        return """
            ___
           /___\\
           \   /
            \ /
             😀
            /|\\
            / \\
​
​
​
        🌿🌿🌿🌿🌿🌿
        """
​
    def _level_3(self):
        """Draws a parachute when user looses the first attempt
        """
        return """
           /___\\
           \   /
            \ /
             🤨
            /|\\
            / \\
​
​
        🌿🌿🌿🌿🌿🌿
        """
​
    def _level_2(self):
        """Draws a parachute when user looses the second attempt
        """
        return """
           \   /
            \ /
             😒
            /|\\
            / \\
​
        🌿🌿🌿🌿🌿🌿
        """
​
    def _level_1(self):
        """Draws a parachute when user looses the third attempt.
        """
        return """
            \ /
             😧
            /|\\
            / \\
        🌿🌿🌿🌿🌿🌿
        """
​
    def _level_0(self):
        """ Displays the game over picture.
        """
        return """
             😵
            /|\\
            / \\
        🔥🔥🔥🔥🔥
        """