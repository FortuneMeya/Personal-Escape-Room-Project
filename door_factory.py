from abc import abstractmethod


class DoorFactory:
    @abstractmethod
    def create_door(self):
        pass
