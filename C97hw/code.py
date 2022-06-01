import random
number = random.randint(1,10)
chances = 5
print("Number Guessing Game")
print("Guess a number between 1 and 10. you have 5 chances!7")

if chances == 5:
    guess = int(input("Enter your guess: ")) 
    
    if guess>number :
        print("Too big!")
        chances = chances - 1
    elif guess<number :
        print("Too small!")
        chances = chances - 1
    else :
        print("YOU WON!!")

          
if chances == 4:
    guess = int(input("Try Again : "))
    
    if guess>number :
        print("Too big!")
        chances = chances - 1
    elif guess<number :
        print("Too small!")
        chances = chances - 1
    else :
        print("YOU WON!!")

if chances == 3:
    guess = int(input("Try Again : "))
    
    if guess>number :
        print("Too big!")
        chances = chances - 1
    elif guess<number :
        print("Too small!")
        chances = chances - 1
    else :
        print("YOU WON!!")
        
if chances == 2:
    guess = int(input("Try Again : ")) 
    
    if guess>number :
        print("Too big!")
        chances = chances - 1
    elif guess<number :
        print("Too small!")
        chances = chances - 1
    else :
        print("YOU WON!!")

if chances == 1:
    guess = int(input("Try Again : ")) 
    
    if guess>number :
        print("Too big!")
        chances = chances - 1
    elif guess<number :
        print("Too small!")
        chances = chances - 1
    else :
        print("YOU WON!!")

if  chances == 0:
        print("YOU LOSE! The number is", number)
else :
        print("YOU LOSE! The number is", number)        