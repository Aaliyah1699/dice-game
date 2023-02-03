'''Roll Dice Game'''
# import random module
import random
# import os module to clear screen after dice are rolled
import os

# Function to pick number if dice


def dice_num():
    while True:# while True loop
        try:#Try get user input for number of dice
            pick_dice = input('Number of Dice: ')
            valid = ['one', 'two']#var list with valid responses
            if pick_dice not in valid:#If response not valid
                raise ValueError('Pick one or two dice.')#raise value error with explanation
            else:# Else return function
                return pick_dice
        except ValueError as err:# Except with value error as err and print err
            print(err)

# Function to roll the dice


def roll_dice():
    min_val = 1# min value of dice
    max_val = 6# max value of dice
    roll_again = 'yes'# roll dice again option
    while roll_again.lower() == 'yes':# While roll again is yes
        os.system('cls' if os.name == 'nt' else 'clear')# use os to clear screen
        amount = dice_num()#call amount dice num func
        # if user choses 2 dice print values and sum of dice
        if amount == 'two':
            print('Lets roll the dice...')
            dice1 = random.randint(min_val, max_val)
            dice2 = random.randint(min_val, max_val)
            # print values and sum of dice
            print('Dice One: ', dice1)
            print('Dice Two: ', dice2)
            print('Total: ', dice1 + dice2)
            roll_again = input('Want to roll again? ') # Ask if they want to roll again
        else:# else if the pick one dice
            print('Lets roll the die...')
            dice1 = random.randint(min_val, max_val)
            print(f'The value is: {dice1}')#print value with f string
            roll_again = input('Want to roll again? ')

# execute func if its called
if __name__ == '__main__':
    roll_dice()
