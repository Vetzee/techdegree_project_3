import os
import random
import time

from phrase import Phrase
from const import PHRASES


class Game:
    def __init__(self, phrases):
        self.phrases = [Phrase(phrase) for phrase in phrases.copy()]
        self.current = random.choice(self.phrases)
        self.guesses = []
        self.lives = 5

    def menu(self):
        print("** Welcome to Phrase Hunter **")
        print("Rules: guess a letter and complete the phrase to win")
        print("Lives remaining: {}\n".format(self.lives))
        # will show the phrase with _ unless guessed
        self.current.show_phrase()
        print()

    def player_guess(self):
        # gets the guesses plus some logic for any 'wrong' guesses
        guess = ''
        while not guess:
            player_guess = input("Enter a guess: ")
            if len(player_guess) > 1:
                print("Too many characters, try again.")
                continue
            elif player_guess.isdigit() or not player_guess.isalpha():
                print("Must be a letter, try again.")
                continue
            elif player_guess.lower() in self.guesses:
                print("You already guessed that, try again.")
                continue
            else:
                guess = player_guess
        self.guesses.append(guess)
        if guess.lower() not in [letter.original.lower() for letter in self.current]:
            self.lives -= 1
        return guess.lower()

    def game_won(self):
        # checks if the entire phrase was guessed
        if self.current.fully_guessed():
            self.clear_screen()
            print("You won!")
            return True
        return False

    def play_again(self, answer):
        # if player want to play again, it runs all over again
        # else it exits
        self.answer = answer
        if self.answer.lower() == 'y' or self.answer.lower() == 'yes':
            return Game(PHRASES).main()
        else:
            self.clear_screen()
            print("Thank you for playing. Have a great day!\n")
            time.sleep(4)
            exit()

    def main(self):
        # loops till game has been one or lost
        while not self.game_won():
            self.clear_screen()
            self.menu()
            player_guess = self.player_guess()
            for item in self.current:
                item.single_string(player_guess)
            if self.lives == 0:
                self.clear_screen()
                self.menu()
                self.play_again(input("You lost :(, would you like to play again? y/n "))
                break
        self.play_again(input("Would you like to play again? y/n "))

    @staticmethod
    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")



