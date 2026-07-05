# import random module for assigning computer for random coices
import random

computer = random.choice([1, -1, 0])
your_choice = input("enter your choice : ").lower() #input from player
youdict = {"snake":1, "water":-1, "gun":0} #dictonaries with options
reverse_dict = {1:"snake", -1 :"water", 0 :"gun"} #revesrse dict we made for just showing the options that players chose

you = youdict[your_choice]
# until now we have two choices which we allready assigned to different variables

#now we will print the choices from the computer and the player 
print(f"you choose {reverse_dict[you]}\ncomputer choose {reverse_dict[computer]}")

#here we defines logic of the whole program

if (computer == you):
    print("🙅‍♂️  its a DRAW")

else:
    if (you == 1 and computer == 0):
        print("☹️  you lost")

    elif (you == 1 and computer == -1):
        print("🎉  you win")

    elif (you == 0 and computer == 1):
        print("🎉  you win")

    elif (you == 0 and computer == -1):
        print("☹️  you lost")

    elif (you == -1 and computer == 1):
        print("☹️  you lost")

    elif (you == -1 and computer == 0):
        print("🎉  you win")

    else:
        print("something went wrong")
    