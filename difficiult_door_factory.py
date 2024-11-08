import random
from combo_door import ComboDoor
from door_factory import DoorFactory
from dead_bolt_door import DeadboltDoor
from code_door import CodeDoor


#from dead_bolt_door import DeadBoltDoor
#from code_door import CodeDoor

class DifficultDoorFactory(DoorFactory):
    def create_door(self):
        difficult_door_list =[ComboDoor(),DeadboltDoor(),CodeDoor()]
        return random.choice(difficult_door_list)
