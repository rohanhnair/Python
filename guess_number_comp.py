import random
import os

user_guess = None

def playerInput():
    global user_guess
    user_guess = int(input('Pick a number between 1-100: '))

def checkNumb():
    if user_guess == random_numb:
        print('You guessed it!')
        return True
    if user_guess > random_numb:
        print('Too high! Guess again')
        return False
    if user_guess < random_numb:
        print('Too low! Guess again')
        return False
        

random_numb = random.randint(0,99)

while user_guess != random_numb:
    playerInput()
    os.system('cls')
    checkNumb()

