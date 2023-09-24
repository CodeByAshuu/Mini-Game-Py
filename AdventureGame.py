'''
Made By: SAGAR SAHU
@Twitter : Ashuuu_7
@LinkedIn : www.linkedin.com/in/sagarr7
'''

#LEARNING PURPOSE (nested if elif else statement)
import time

name=input("Enter your name last survivor: ")
print("Welcome",name,"to the Mysterious Cave Adventure!")
time.sleep(1)
print("You find yourself standing at the entrance of a dark cave.")
time.sleep(1)
print("Your mission is to explore the cave and find the hidden treasure.")
time.sleep(1)
print("But beware, there are dangers lurking inside!\n")

# Start of the adventure
print("You have entered the cave.")
time.sleep(1)

# First choice
print("You see three paths in front of you.")
print("1. Go left into a narrow tunnel.")
print("2. Go right and follow a dimly lit corridor.")
print("3. Walk straight ahead into a dark chamber.")
choice1 = input("Enter 1, 2, or 3: ")

if choice1 == "1":
    # Second choice
    print("The narrow tunnel leads you to a fork in the path.")
    print("1. Take the path that goes up steeply.")
    print("2. Take the path that descends deeper into the cave.")
    choice2 = input("Enter 1 or 2: ")

    if choice2 == "1":
        print("You climb up the steep path and reach a hidden ledge.")
        time.sleep(2)
        print("On the ledge, you find a chest full of gems!")
        time.sleep(2)
        print("Congratulations! You've found the treasure!")

    elif choice2 == "2":
        print("You descend deeper into the cave, but it leads to a dead end.")
        time.sleep(2)
        print("You must turn back and choose another path.")

    else:
        print("Invalid choice. You're lost in the cave!")

elif choice1 == "2":
    # Third choice
    print("You follow the dimly lit corridor and come across a fork in the path.")
    print("1. Take the path that goes left into a narrow crevice.")
    print("2. Continue down the corridor.")
    choice3 = input("Enter 1 or 2: ")

    if choice3 == "1":
        print("The narrow crevice leads you to a hidden underground lake.")
        time.sleep(2)
        print("You spot a boat by the shore and row to the center of the lake.")
        time.sleep(2)
        print("In the middle of the lake, you find a chest filled with treasures!")
        time.sleep(2)
        print("Congratulations! You've found the treasure!")

    elif choice3 == "2":
        print("You continue down the corridor but suddenly fall into a pit trap!")
        time.sleep(2)
        print("You'll have to find a way out of the pit first.")

        # Fourth choice
        print("In the pit, you notice two tunnels.")
        print("1. Crawl through the narrow tunnel on the left.")
        print("2. Climb up the rocky path on the right.")
        choice4 = input("Enter 1 or 2: ")

        if choice4 == "1":
            print("The narrow tunnel leads you to a hidden passage.")
            time.sleep(2)
            print("After a while, you find a chest filled with gold!")
            time.sleep(2)
            print("Congratulations! You've found the treasure!")

        elif choice4 == "2":
            print("You climb up the rocky path and reach a dead end.")
            time.sleep(2)
            print("You must climb back down and choose another path.")

        else:
            print("Invalid choice. You're still in the pit!")

    else:
        print("Invalid choice. You're lost in the cave!")

elif choice1 == "3":
    # Fifth choice
    print("You enter the dark chamber and find yourself in complete darkness.")
    print("1. Light a torch and explore the chamber.")
    print("2. Try to navigate the darkness without a torch.")
    choice5 = input("Enter 1 or 2: ")

    if choice5 == "1":
        print("With the torch, you discover a hidden passage in the chamber.")
        time.sleep(2)
        print("Following the passage, you find a chest filled with ancient relics!")
        time.sleep(2)
        print("Congratulations! You've found the treasure!")

    elif choice5 == "2":
        print("You stumble around in the darkness and accidentally trigger a trap!")
        time.sleep(2)
        print("Darts shoot out from the walls, and you are hit.")
        time.sleep(2)
        print("Injured and disoriented, you'll need to find a way out of the chamber.")

        # Sixth choice
        print("You feel your way around and discover two exits.")
        print("1. Take the left exit.")
        print("2. Take the right exit.")
        choice6 = input("Enter 1 or 2: ")

        if choice6 == "1":
            print("You take the left exit and find a hidden path.")
            time.sleep(2)
            print("After a while, you find a chest filled with precious stones!")
            time.sleep(2)
            print("Congratulations! You've found the treasure!")

        elif choice6 == "2":
            print("You take the right exit and find yourself in a dead-end alcove.")
            time.sleep(2)
            print("You must retrace your steps and choose another path.")

        else:
            print("Invalid choice. You're still in the dark!")

    else:
        print("Invalid choice. You're lost in the cave!")

else:
    print("Invalid choice. The cave's dark forces consume you! You are DEAD")

print("\nThanks for playing the Mysterious Cave Adventure!",name)


"""
TO WIN THE GOLD:

1. Choose option "2" at the start to go right and follow the dimly lit corridor.
2. After that, choose option "1" to take the left path into a narrow crevice.
3. In the crevice, choose option "1" again to row the boat to the center of the underground lake.
4. At the lake's center, choose option "1" to crawl through the narrow tunnel on the left.
5. Following the narrow tunnel, you will eventually find a chest filled with gold, and congratulations, you've found the treasure!

"""