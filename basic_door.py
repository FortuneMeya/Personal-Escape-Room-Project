from door import  Door
import random

class BasicDoor(Door):
    def __init__(self):
        self._solution = random.randint(1, 2)
        self._input = 0

    def examine_door(self):
        return f'A basic door. You can either push or pull it to open.'

    def menu_options(self):
        return f'1. Push\n2. Pull'

    def get_menu_max(self):
        return 2

    def attempt(self, option):
        self._input = option
        if self._input == 1:
            return print('You push the door.')
        else:
            return print('You pull the door.')

    def is_unlocked(self):
        if self._input == self._solution:
            return True
        else:
            return False

    def clue(self):
        return print("Try the other way.")

    def success(self):
        return print("You found the correct value and opened the door.")