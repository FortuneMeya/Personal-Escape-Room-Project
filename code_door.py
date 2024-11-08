import random

from door import Door


class CodeDoor(Door):
    def __init__(self):
        self._solution = random.randint(1, 3)
        self._input = 0

    def examine_door(self):
        return f'A door with a coded keypad with three characters. Each key toggles a value with an X or an O'

    def menu_options(self):
        return f'1.Press Key 1\n2.Press Key 2\n3.Press Key 3'

    def get_menu_max(self):
        return 3

    def attempt(self, option):
        self._input = option
        if self._input == 1:
            return print('You pressed key 1.')
        elif self._input==2:
            return print('You pressed key 2.')
        elif self._input==3:
            return print('You pressed key 3')
        else:
            return print('Invalid input')

    def is_unlocked(self):
        if self._input == self._solution:
            return True
        else:
            return False

    def clue(self):
        if self._input != self._solution:
            print('Which characters are correct.')


    def success(self):
        if self._input == self._solution:
            print('You have successfully found the key')
        else:
            print(f'You have yet to find the key')







