from door import  Door
import random

class ComboDoor(Door):
    def __init__(self):
        self._solution = random.randint(1, 10)
        self._input = 0

    def examine_door(self):
        return f'A door with a combination lock. You can spin the dial to a number 1- 10.'

    def menu_options(self):
        return f'Enter # 1-10:'

    def get_menu_max(self):
        return 10

    def attempt(self, option):
        self._input = option
        return print(f'You turn the dial to... {self._input}')

    def is_unlocked(self):
        if self._input == self._solution:
            return True
        else:
            return False

    def clue(self):
        if self._input > self._solution:
            return print('Try a lower value.')
        elif self._input < self._solution:
            return print('Try a higher value.')

    def success(self):
        return print("You found the correct value and opened the door.")