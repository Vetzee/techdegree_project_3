from character import Character


class Phrase:
    def __init__(self, phrase):
        # A phrase should be a collection of Character objects, where
        # each letter of the phrase is a Character() instance stored inside
        # a collection such as a List.
        self.phrase = phrase
        self.phrase = [Character(letter) for letter in self.phrase]

    def __iter__(self):
        # basically makes s.p an iter and yields one object at a time
        yield from self.phrase

    def fully_guessed(self):
        # will check to see if the entire phrase was guessed
        guessed = []
        for self.letter in self.phrase:
            if self.letter.was_guessed:
                guessed.append(self.letter)
        if len(guessed) == len(self.phrase):
            return True

    def show_phrase(self):
        # will show the phrase
        for letter in self.phrase:
            print(letter.hidden(), end='')

