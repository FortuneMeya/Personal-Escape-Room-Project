"""
Escape Room


November 7th, 2024


Fortune Meya
Yusuke Homma

User have to open the three doors to escape. There are five different kinds of doors and doors that user will encounter will be
changed based on the difficulty.
"""



from easy_door_factory import EasyDoorFactory
from difficiult_door_factory import DifficultDoorFactory

def main():
    print("Welcome to the Escape Room. You must unlock 3 doors to escape...")
    difficulty = input("Enter Difficulty (1. Easy 2. Hard): ")
    numbers_of_doors_attempted = 0

    while numbers_of_doors_attempted < 3:
        if difficulty == "1":
            door_factory = EasyDoorFactory()
        else:
            door_factory = DifficultDoorFactory()

        door = door_factory.create_door()

        unlocked = False
        while not unlocked:
            print(door.menu_options())
            try:
                option = int(input("Choose an option: "))
                door.attempt(option)
                if door.is_unlocked():
                    door.success()
                    unlocked = True
                    numbers_of_doors_attempted += 1
                else:
                    door.clue()
            except ValueError:
                print("Please enter a valid number.")

        print(f"Doors unlocked so far: {numbers_of_doors_attempted}/3\n")

    print("Congratulations! You have escaped!")

main()
