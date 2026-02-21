while True:
 def my_func1():
  for i in range(0,2):
   print("")
 def my_func2():
  for i in range(0,2):
   print("-------------------------------")
 def cong():
  print("Congratulations")
  print("")
  print("You Win")
 def loss():
  print("your guess",guess,"is wrong")
  print("")
  print("You Loss")
 my_func1()   
 my_func2()
 my_func1()
 print ('  Welcome to number Guessing game')
 my_func1()
 my_func2()
 my_func1()
 print("Before the start of game we need following information from you")
 my_func1()
 my_func2()
 my_func1()
 num= (input("Enter Your Name:  "))
 age= eval(input("Enter Your age:    "))
 if age>0:
    print("")
    print("Now play your game!")
    my_func1()
    print("There are 3 levels.")
    print("Chose one of them")
    print("")
    def level():
     class levels:
      level_1= "1. 😀Easy:   1 - 20 ➡️"
      level_2= "2. 😐Medium: 21- 50 ➡️"
      level_3= "3. 😵Hard:   51-100 ➡️"
     print(levels.level_1)
     print(levels.level_2)
     print(levels.level_3)
    level()
    print("")
    level_num= eval(input("Type the number of the level you like: "))
    print("")
    if level_num==1:
      print("")
      guess= (eval(input("Enter Your guess between 1-20:    ")))
      print("")
      import random
      guess_number= random.randint(1,20)
      if guess==guess_number:
        print("Your guess",guess_number," is right")
        cong()
      else:
        loss()
    elif level_num==2:
      guess= eval(input("Enter Your guess between 21-50:     "))
      print("")
      import random
      guess_number= random.randint(21,50)
      if guess==guess_number:
        print("Your guess",guess_number," is right")
        cong()
      else:
        loss()
    elif level_num==3:
      guess= (eval(input("Enter Your guess between 51-100:    ")))
      print("")
      import random 
      guess_number= random.randint(51,100)
      if guess==guess_number:
        print("Your guess",guess_number," is right")
        cong()
      else:
        loss()
    else:
      print("Put level number")
 else:
    print("You have put wrong age.")
    print("execute program again and enter right age")
 for i in range(0,4):
    print("============================================")
    
    
 