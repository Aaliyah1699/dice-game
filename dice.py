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