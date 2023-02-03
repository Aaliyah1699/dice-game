'''Roll Dice Game'''
#import random module
import random
#import os module to clear screen after dice are rolled
import os

#Function to pick number if dice
def dice_num():
    #while True loop 
    while True:
        #Try - get user input for number of dice & a var list with valid responses
        try:
            pick_dice = input('Number of Dice: ')
            valid = ['1','one','2', 'two']
            #If input not in valid response raise value error with explanation
            if pick_dice not in valid:
                raise ValueError('Pick 1 or 2 dice.')
            #Else return function
            else:
                return dice_num()
        #Except with value error as err and print err
        except ValueError as err:
            print(err)

#Function to roll the dice
def roll_dice():
    #min value of dice
    min_val = 1
    #max value of dice
    max_val = 6
    #roll dice again option
    roll_again = 'y'

    #While roll again is yes call amount dice num
    while roll_again.lower() == 'yes' or roll_again.lower() == 'y':
        # use os to clear screen 
        os.system('cls' if os.name == 'nt' else 'clear')
        amount = dice_num()

        #if user choses 2 dice print values and sum of dice
        if amount == '2' or amount == 'two':
            print('Lets roll the dice...')
            dice1 = random.randint(min_val, max_val)
            dice2 = random.randint(min_val, max_val)
            #print values and sum of dice
            print('Dice One: ',dice1)
            print('Dice Two: ',dice2)
            print('Total= ', dice1 + dice2)
            #Ask if they want to roll again
            roll_again = input('Want to roll again? ')
