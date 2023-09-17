#--- ROCK PAPER SCISSOR GAME ---

'''
Made By : Sagar Sahu
@Twitter : Ashuuu_7
@LinkedIn : www.linkedin.com/in/sagarr7
@Instagram : ashhuu.u

'''

from random import randint

list = ['r','p','s']

computer = list[randint(0,2)]

#Player var declared
player = False

#-- ASCII art for rock,paper and scissors--
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
line = "****************************************\n"

#-- Game Logic --
while player == False:
    player = input("Rock, Paper, Scissors? (r/p/s/x for exit): ")
    if player == computer:
        print("Tie!")
    elif player == "r":
        if computer == "p":
            print(line)
            print("You lose!"+ paper)
            print("covers", rock)
            print(line)
        else:
            print(line)
            print("You win!" + rock) 
            print("smashes" + scissors)
            print(line)
    elif player == "p":
        if computer == "s":
            print(line)
            print("You lose!" + scissors) 
            print("cut" + paper)
            print(line)
        else:
            print(line)
            print("You win!" + paper) 
            print("covers"+ rock)
            print(line)
    elif player == "s":
        if computer == "Rock":
            print(line)
            print("You lose..." + rock )
            print("smashes" + scissors)
            print(line)
        else:
            print(line)
            print("You win!" + scissors) 
            print("cut" + paper)
            print(line)
    elif player == "x":    
        # Add a termination condition
        print("Consider playing this game again")
        break
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues ever..
    player = False
    computer = list[randint(0,2)]

''' 
Write code here
Game sequence
'''