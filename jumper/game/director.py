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
        current_letter: Current letter entered by the player
        guessed_letters: Letters of the secret word that the player has guessed.
    """

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """
        self._secret_word = SecretWord()
        self._parachute = Parachute()
        self._is_playing = True
        self._terminal_service = TerminalService()
        self._current_letter = ''
        self._guessed_letters = []

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """

        welcome = """
                __
                \ \ _   _ _ __ ___  _ 🪂   ___ _ __
     *******     \ \ | | | '_ ` _ \| '_ \ / _ \ '__|  *******
     *******  /\_/ / |_| | | | | | | |_) |  __/ |     *******
              \___/ \__,_|_| |_| |_| .__/ \___|_|
                                   |_|
        """

        self._terminal_service.write_text(welcome)

        #Generate the secret word
        self._secret_word.input_word(self._terminal_service)
        print(self._secret_word.get_word())
        # print(self._secret_word.get_word_letters())

        while self._is_playing:
            self._do_outputs()
            self._get_inputs()
            self._do_updates()


            #self._found_letter = self._secret_word.check_letter(
            #    word, input(letter), lines)
            #self._secret_word.display_progress(lines)
#
            #if self._found_letter == 'no':
            #    self._no_found_letter += 1
#
            #is_found = self._secret_word.if_found(lines)
#
            #if is_found == 'yes':
            #    print('You win')
            #    break
            #elif self._no_found_letter == 4:
            #    print('You lose')
            #    break
            #else:
            #    continue

    def _get_inputs(self):
        """Get a letter from the player.

        Args:
            self (Director): An instance of Director.
        """
        self._current_letter = self._terminal_service.read_text("Guess a letter [a-z]: ")

    def _do_updates(self):
        """Keeps watch on the letters entered and lives of the player.

        Args:
            self (Director): An instance of Director.
        """
        if self._secret_word.check_letter(self._current_letter):
            self._guessed_letters.append(self._current_letter)
            if self._secret_word.is_found(self._guessed_letters):
                self._is_playing = False
                self._terminal_service.write_text("\nYou made it!")
        else:
            self._parachute.lose_life()
            lifes = self._parachute.get_lifes()
            if lifes == 0:
                self._is_playing = False
                self._terminal_service.write_text("\nYou lost. I'm sorry :(")

    def _do_outputs(self):
        """Displays game progress and draw the parachute.

        Args:
            self (Director): An instance of Director.
        """
        #Printing display progress (guessed_letters)
        self._secret_word.display_progress(self._guessed_letters, self._terminal_service)

        #Printing parachute
        self._parachute.draw_image(self._terminal_service)

