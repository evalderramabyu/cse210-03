from game.terminal_service import TerminalService
import random


class SecretWord:

    def __init__(self):
        """Constructs a new Jumper.

        Args:
            self (Jumper): An instance of Jumper.
        """
        self._word = ''
        self._letter = ''
        self._word_letters = []
        self._word_level = ''
        self._terminal_service = TerminalService()

    def _basic_level(self):
        """
            Select a random basic word

            Args:
                self (SecretWord): An instance of SecretWord.

            Returns: 
                self._word: The random word
        """

        list_words = ['feel', 'glad', 'down', 'time',
                      'duck', 'long', 'part', 'fast', 'cake', 'city']
        self._word = random.choice(list_words)
        return self._word

    def _intermediate_level(self):
        """
            Select a random intermediate word

            Args:
                self (SecretWord): An instance of SecretWord.

            Returns: 
                self._word: The random word
        """

        list_words = ['author', 'century', 'design', 'unique',
                      'create', 'debate', 'theory', 'vision', 'relax', 'flexible']
        self._word = random.choice(list_words)
        return self._word

    def _advanced_level(self):
        """
            Select a random advanced word

            Args:
                self (SecretWord): An instance of SecretWord.

            Returns: 
                self._word: The random word
        """

        list_words = ['indubitable', 'propitious', 'reciprocate', 'infallible',
                      'jeopardize', 'antiquated', 'quotidian', 'hazardous', 'impeccable', 'syllogism']
        self._word = random.choice(list_words)
        return self._word

    def _empty_word(self, number):
        """
            Create lines depending the number of letter in the random word

            Args:
                self (SecretWord): An instance of SecretWord.

            Returns: 
                self._word_letters: The word like lines

        """

        for i in range(number):
            self._word_letters.append('_')
        return self._word_letters

    def input_word(self):
        """
            Select a random 

            Args:
                self (SecretWord): An instance of SecretWord.

            Returns: 
                self._word: The random word (basic, intermediate or advanced)
                self._word_level:   1 for basic word
                                    2 for intermediate word
                                    3 for advanced word
        """

        self._word_level = random.randint(1, 3)

        if self._word_level == 1:
            self._terminal_service.write_text(
                'This is your lucky day, your word is very easy to guess 👏')
            self._word = self._basic_level()

        elif self._word_level == 2:
            self._terminal_service.write_text(
                'You can guess this work, only think a little bit 👍')
            self._word = self._intermediate_level()

        else:
            self._terminal_service.write_text(
                'This word is very difficult. Do you really think you can guess it? 😏')
            self._word = self._advanced_level()

        self._word_letters = self._empty_word(len(self._word))

        return self._word, self._word_letters

    def check_letter(self, random_word, selected_letter, lines):
        found_letter = 'no'
        for i in range(len(random_word)):
            if random_word[i] == selected_letter:
                lines[i] = selected_letter
                found_letter = 'yes'
        return found_letter

    def if_found(self, lines):
        found = 'yes'
        for i in range(len(lines)):
            if lines[i] == '_':
                found = 'no'
        return found

    def display_progress(self, lines):
        print('⚕️', end=' ')
        for i in range(len(lines)):
            print(f' {lines[i]}', end=' ')
        print('\n❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️\n')
