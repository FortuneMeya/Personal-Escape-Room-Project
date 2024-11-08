import random

from door import Door


class DeadboltDoor(Door):
    def __init__(self):
        self._solution=random.randint(1,2)
        self._input =0

    def examine_door(self):
        return f'A double deadbolt door. Both need to be unlocked to open the door, but you can’t tell by looking at them if they’re locked or unlocked.'
    def menu_options(self):
        return f'1.Toggle bolt 1\n2.Toggle bolt 2'
    def get_menu_max(self):
        return 2

    def attempt(self, option):
        self._input = option
        if self._input == 1:
            return print('You have toggle bolt 1.')
        elif self._input ==2:
            return print('You have toggle bolt 2.')
        else:
            print('Invalid input')
    def is_unlocked(self):
        if self._input==self._solution:
            return True
        else:
            return False

    def clue(self):
        if self._input != self._solution:
            print('You jiggle the door.... it seems like one the bolts is unlocked')
        else:
            print('It seems like it is completely locked')

    def success(self):
        if self._input == self._solution:
            print('You have successfully found the key')
        else:
            print(f'You have yet to find the key')







