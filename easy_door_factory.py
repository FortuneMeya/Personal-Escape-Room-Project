import random
from basic_door import BasicDoor
from door_factory import DoorFactory
from locked_door import LockedDoor
from combo_door import ComboDoor

class EasyDoorFactory(DoorFactory):
    def create_door(self):
        door_list =[BasicDoor(),LockedDoor(),ComboDoor()]
        return random.choice(door_list)