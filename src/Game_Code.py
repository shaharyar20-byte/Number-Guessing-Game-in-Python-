print('  Welcome to Number Guessing Game')
print("Hello! Now play your game!")

import random
guess= (eval(input("Enter Your guess between 1-20:    ")))
guess_number= random.randint(1,20)
if (guess==guess_number):
  print("Congratulations",name,"your guess is correct")
  print("You Win")
elif guess<1 or guess>20:
  print("You guess is out of range. Put guess between 1 and 20")
else:
  print("your guess is wrong")
  print("You Loss")