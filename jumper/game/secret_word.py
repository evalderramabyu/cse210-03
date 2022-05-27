from game.terminal_service import TerminalService
import random


class SecretWord:

    def __init__(self):
        """Constructs a new Jumper.

        Args:
            self (Jumper): An instance of Jumper.
        """
        self._word = ''
        self._word_letters = []

    def get_word(self):
        return self._word

    def get_word_letters(self):
        return self._word_letters

    def _basic_level(self):
        """
            Select a random basic word

            Args:
                self (SecretWord): An instance of SecretWord.

            Returns:
                string: A random word.
        """
        list_words = [
            ("feel", "🙂​"),
            ("glad", "😊​​"),
            ("down", "⬇️​​"),
            ("time", "⌚​"),
            ("duck", "📃​​"),
            ("long", "📏​​"),
            ("part", "🧁​​"),
            ("fast", "🏎️​​"),
            ("cake", "🕯️​​"),
            ("city", "🌉​​"),
        ]

        return random.choice(list_words)

    def _intermediate_level(self):
        """
            Select a random intermediate word

            Args:
                self (SecretWord): An instance of SecretWord.

            Returns:
                string: A random word.
        """

        list_words = [
            ("author","✍️​"),
            ("adventure","🗺️​"),
            ("design","🖊️​"),
            ("unique","💎​"),
            ("create","🎨​"),
            ("celebrate","🎆​"),
            ("theory","🎩​"),
            ("vision","👓​"),
            ("relax","🏖️​"),
            ("flexible","🦿​"),
        ]

        return random.choice(list_words)

    def _advanced_level(self):
        """
            Select a random advanced word

            Args:
                self (SecretWord): An instance of SecretWord.

            Returns:
                string: A random word.
        """

        list_words = [
            ("indubitable","🤔​"),
            ("propitious","⛈️​"),
            ("reciprocate","🤝​"),
            ("infallible","🔮​"),
            ("jeopardize","♟️​"),
            ("antiquated","🧝​"),
            ("quotidian","🗞️ ⏰​​"),
            ("hazardous","🎲​"),
            ("impeccable","💅🤵​​"),
            ("syllogism","💭🧠​​")
        ]

        return random.choice(list_words)

    def input_word(self, terminal_service):
        """
            Select a random

            Args:
                self (SecretWord): An instance of SecretWord.
        """

        word_level = random.randint(1, 3)   # 1 for basic word
                                            # 2 for intermediate word
                                            # 3 for advanced word
        secret_word = ''

        if word_level == 1:
            terminal_service.write_text(
                'This is your lucky day, your word is very easy to guess 👏 \n')
            secret_word = self._basic_level()

        elif word_level == 2:
            terminal_service.write_text(
                'You can guess this work, only think a little bit 👍 \n')
            secret_word = self._intermediate_level()

        else:
            terminal_service.write_text(
                'This word is very difficult. Do you really think you can guess it? 😏 \n')
            secret_word = self._advanced_level()

        self._word = secret_word[0]
        self._word_letters = list(secret_word[0])

        terminal_service.write_text(f"This emoji is your hint: {secret_word[1]}")
        terminal_service.write_text(f"The word has {len(secret_word[0])} letters")
        terminal_service.write_text("You have 4 lives")

    def check_letter(self, letter):
        return letter in self._word_letters

    def is_found(self, guessed_letters):
        word_1 = sorted(guessed_letters)
        word_1 = list(set(word_1))
        word_2 = sorted(self._word_letters)
        word_2 = list(set(word_2))
        return word_1 == word_2

    def display_progress(self, guessed_letters, terminal_service):
        terminal_service.write_text("")
        for i in range(len(self._word_letters)):
            letter = self._word_letters[i]
            if letter in guessed_letters:
                print(f' {letter} ', end=' ')
            else:
                print('_ ', end=' ')
        terminal_service.write_text("")
