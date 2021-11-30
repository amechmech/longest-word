# game.py
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

import string
import random

class Game:
    def __init__(self):
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))
    
    def is_valid(self, word):
        if not word:
            return False
        letters = self.grid.copy() # Consume letters from the grid
        #print(f'word is {word}')
        #print(f'letters initial is {letters}')
        for letter in word:
            if letter in letters:
                letters.remove(letter)
                #print(f'letters ongoing is {letters}')
            else:
                return False
        return True