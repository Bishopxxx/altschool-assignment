#ths is a guessing game
import random


life = 3
i = random.randint(4,7)


while True:
    guess = int(input("Enter a number: "))

    if life == 0:
        print("You have exhausted your trials") 
        print (" The computer predicted " + str(i) + " as the number")6
        break
    elif life == 1:
        print("You have 1 trial left")
        life -= 1
    elif i < guess:
        print ("The computer predicted a lesser number. You are have " + str(life) + " trials left")
        life -= 1
    elif i > guess:
        print ("The computer predicted a greater number. You are have " + str(life) + " trials left")
        life -= 1
    else:
        print ("Congratulations!!! The computer predicted " + str(i) + " as you have predicted.")
        break
