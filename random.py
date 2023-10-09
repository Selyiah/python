# Random

import random
random_integer = random.randint(1, 100)
print(random_integer)

# The randint() function generates a random number between two values
# This program uses randint() to simulate dice with any number of sides

import random
sides = int(input('How many sides does the dice have? '))
random_integer = random.randint(1, sides)
print('You rolled a {}'.format(random_integer))

# head or tails
import random
def flip_coin():
    random_number = random.randint(1, 2)
    if random_number == 1:
      side = 'heads'
    else:
      side = 'tails'
    return side
choice = input('heads or tails: ')
result = flip_coin()
print('The coin landed on {}'.format(result))

# rock, paper, scissors

import random
def random_choice():
    choice_number = random.randint(1, 3)
    if choice_number == 1:
      choice = 'rock'
    elif choice_number == 2:
      choice = 'scissors'
    else:
      choice = 'paper'
    return choice
my_choice = input('Choose rock, scissors or paper: ')
opponent_choice = random_choice()
print('Your opponent chose {}'.format(opponent_choice))
if my_choice == 'rock' and opponent_choice == 'scissors':
    print('You win!')

# roulette

import random

def colour():
    random_number = random.randint(1, 2)
    if random_number == 1:
      colour = 'red'
    else:
      colour = 'black'
    return colour

random_number = random.randint(1, 100)
random_colour = colour()

