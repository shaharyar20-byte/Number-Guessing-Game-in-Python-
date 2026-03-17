print('  Welcome to Number Guessing Game')
print("Before the start of game we need following information from you")
name= str(input("Enter Your Name:  "))
print("Hello!",name,"Now play your game!")

import random
guess= (eval(input("Enter Your guess between 1-20:    ")))
guess_number= random.randint(1,20)
if (guess==guess_number):
print("Congratulations",name,"your guess is correct")
print(name,"You Win")
elif guess<1 or guess>20:
print("You guess is out of range. Put guess between 1 and 20")
else:
print(name,"your guess is wrong")
print("You Loss")

Check it. It's first initial version