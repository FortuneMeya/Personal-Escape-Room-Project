import random

from door import Door
class LockedDoor(Door):
    def __init__(self):
        self._solution =random.randint(1,3)
        self._input=0

    def examine_door(self):
        return f'Door is locked, look around to see if the key is hidden nearby'
    def menu_options(self):
        return f'1.Look under the mat.\n2.Look under the flower pot.\n3.Look under the fake rock.'
    def get_menu_max(self):
        return 3
    def attempt(self, option):
        self._input=option
        if self._input==1:
            print('You have attempted to look under the mat.')
        elif self._input==2:
            print('You have attempted to look under the flower pot.')
        elif self._input==3:
            print('You have attempted to look under the fake rock.')
        else:
            print('invalid input')
    def is_unlocked(self):
        if self._input==self._solution:
            return True
        else:
            False
    def clue(self):
        if self._input!=self._solution:
            print('Look somewhere else')
    def success(self):
        if self._input==self._solution:
            print('You have successfully found the key')
        else:
            print(f'You have yet to find the key')








