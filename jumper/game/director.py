from game.parachute import Parachute
from game.secret_word import SecretWord
from game.terminal_service import TerminalService

class Director:
    """A person who directs the game.

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        parachute (Parachute): The game's parachute.
        secret_word (SecretWord): The game's secret_word.
        is_playing (boolean): Whether or not to keep playing.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """
        self._parachute = Parachute()
        self._secret_word = SecretWord()
        self._is_playing = True
        self._terminal_service = TerminalService()

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """
        #Do smothing
