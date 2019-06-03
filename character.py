class Character:

    def __init__(self, original, was_guessed=False):
        # attribute to store the original
        self.original = original
        self.was_guessed = was_guessed

        # this will take care of any whitespace
        if self.original == ' ':
            self.was_guessed = True

    def single_string(self, guess):
        """
        this checks to see if the 'guess' matches the original
        and then returns it
        """
        self.guess = guess
        if self.guess == self.original:
            self.was_guessed = True

    def hidden(self):
        """
        if the guess matched the origianl, it returns the letter
        else it returns an _
        """
        if self.was_guessed:
            return self.original
        else:
            # to make it look more separated'
            return '_ '


