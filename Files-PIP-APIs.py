#Files, PIP, APIs

with open('people.txt', 'w+') as text_file:  # w+ means write & with open is a key word and means you don't have to close it later
    people = "Joanne \nSusan \nAmina"  # \n means new line
    text_file.write(people)  # opens new file so you can read and write

with open('people.txt', 'r') as text_file: # r means read
    contents = text_file.read()
    print(contents)


new_item = input("Enter a to-do item: ")
with open('todo.txt', 'r') as todo_file:
    todo = todo_file.read()

    todo = todo + new_item + '\n'

with open('todo.txt', 'w+') as todo_file:
    todo_file.write(todo)


import csv  # similar to excel

field_names = ['name', 'age']

data = [
    {'name': 'Jill', 'age': 32},
    {'name': 'Sara', 'age': 28},
]

with open('team.csv', 'w+') as csv_file:
    spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names) # DictWriter is a class

    spreadsheet.writeheader()  # this will write the headers into the csv file
    spreadsheet.writerows(data)  # this will write the rows into the csv file

with open('team.csv', 'r') as csv_file:  # read only file
    spreadsheet = csv.DictReader(csv_file)
    for row in spreadsheet:
        print(dict(row))



import csv

with open('tress.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)

    heights = []

    for row in spreadsheet:
        tree_height = row['height']
        heights.append(tree_height)

shortest_height = min(heights)
print(shortest_height)


#PIP

import requests

print()


# APIs - sending data to one another and allows you to interact with other programs
# over the internet

# API request: When your program asks an API for some or to complete a specific action
# API response: the result of your request from the API

import requests
from pprint import pprint

pokemon_number = input("What is the Pokemon's ID? ")

url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)

response = requests.get(url)
print(response)

pokemon = response.json()
pprint(pokemon) # pprint means the data will be printed in a more organised format

# response 200 = Ok = The request worked
# response 404 = not found = couldn't find the url requested
# response 400 = bad request = the request you made isn't understood

import requests

pokemon_number = input("What is the Pokemon's ID? ")

url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)

response = requests.get(url)
pokemon = response.json()

print(pokemon['name'])
print(pokemon['height'])
print(pokemon['weight'])

