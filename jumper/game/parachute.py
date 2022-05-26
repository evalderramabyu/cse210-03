
class Parachute:
    def _init_(self):
        """
        Attributes
            _lives: integer
        """

        self.lives = 4 
        self._level_number = 0

    def lose_life(self):
        """
        Takes a live away from the remaining lives of the game
        """
        self.lives -= 1

    def draw_image(self):
        """Draws a picture of a parachute
        """
        method = 'level_' + str(self._level_number)
        return getattr(self, method)()

    def level_0(self):
        """Draws a complete parachute to start the game
        """
        return """
                ___
               /___\
               \   /
                \ /
                😀
                /|\
                / \  



           🌿🌿🌿🌿🌿 

        """

    def level_1(self):
        """Draws a parachute when user looses the first attempt
        """
        return """
           
               /___\
               \   /
                \ /
                🤨
                /|\
                / \  


            🌿🌿🌿🌿🌿 

        """

    def level_2(self):
        """Draws a parachute when user looses the second attempt
        """        
        return """               
               \   /
                \ /
                😒
                /|\
                / \ 

            🌿🌿🌿🌿🌿 

        """

    def level_3(self):
        """Draws a parachute when user looses the third attempt.
        """
        return """
                \ /
                😧
                /|\
                / \ 
            🌿🌿🌿🌿🌿 
        """

    def level_4(self):
        """ Displays the game over picture.
        """
        return """
                😵
                /|\
                / \ 
            🔥🔥🔥🔥
        """

  