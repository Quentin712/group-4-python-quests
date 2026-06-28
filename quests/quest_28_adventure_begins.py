# quest_28_adventure_begins.py

# each spot in the story is its own function
def forest():
    print("You stand at the edge of a dark forest.")
    choice = input("Do you go in or turn back? (in/back): ")
    if choice == "in":
        cave()
    else:
        print("You turn back and live a quiet, boring life. The end.")

def cave():
    print("Inside the forest you find a cave glowing with light.")
    choice = input("Do you enter the cave or keep walking? (enter/walk): ")
    if choice == "enter":
        print("You find an ancient treasure and become legend. The end.")
    else:
        print("You keep walking and get lost forever. The end.")

# game starts here
forest()
