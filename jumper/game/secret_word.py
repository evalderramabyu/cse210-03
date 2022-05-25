import random


class SecretWord:

    def __init__(self):
        """Constructs a new Jumper.

        Args:
            self (Jumper): An instance of Jumper.
        """
        self._word = ''
        self._word_letters = []
        self._word_level = ''

    def basic_level(self):
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

    def intermediate_level(self):
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

    def advanced_level(self):
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
            print('This is your lucky day, your word is very easy to guess 👏')
            self._word = self.basic_level()

        elif self._word_level == 2:
            print('You can guess this work, only think a little bit 👍')
            self._word = self.intermediate_level()

        else:
            print('This word is very difficult. Do you really think you can guess it? 😏')
            self._word = self.advanced_level()

        return self._word

    def check_letter(self):
        pass

    def if_found(self):
        pass

    def display_progress(self):
        pass
