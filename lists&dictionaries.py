# lists and dictionaries

#A list of integers
#lottery_numbers = [4, 8, 15, 16, 23, 42]
#A list of strings
#student_names = ['Diedre', 'Hank', 'Helena', 'Salome']

student_names = ["Diedre", "Hank", "Helena", "Salome"]
print(student_names[2])
# remember that the number starts from 0 so in this case this is 0-3

student_names = ['Diedre', 'Hank', 'Helena', 'Salome']
student_names[1] = "Mary"
print(student_names)

clothes = ["shorts", "shoes", "t-shirt"]
if clothes[0] == "shorts":
    clothes[0] = "warm coat"

print(clothes)

clothes = [
    "shorts",
    "shoes",
    "t-shirt",
]

drawer_1 = clothes[0]
if drawer_1 == "shorts":
    clothes[0] = "warm coat"

print(clothes)

costs = [1.2, 4.3, 2.0, 0.5]
new_costs = sorted(costs)
desc_costs = list(reversed(new_costs))
print(desc_costs)

shopping_list = ["bread","eggs","Tomatoes","oranges"]
if "bread" in shopping_list:
   shopping_list.append("butter")
   print(shopping_list)
else:
   print("No item called bread in the list")

# this code below doesn't have bread in the shopping list.
shopping_list = ["eggs", "Tomatoes", "oranges"]
if "bread" in shopping_list:
   shopping_list.append("butter")
   print(shopping_list)
else:
   print("No item called bread in the list")

fridge = [
    "cheese",
    "pizza",
    "coke",
]

if "milk" not in fridge:  # "not in" is a python statement like if/else statement
    print("you have no milk in the fridge")

student_names = ["lucy", "priya", "adam", "steve"]
count = 0

for student_name in student_names:
    count = count + 1  #new count starting from 1 instead of 0
print(count)


costs = [8.30, 7.12, 5.01, 1.00, 0.99, 5.92, 3.50]
total_cost = 0

for lunch_cost in costs:
    total_cost = total_cost + lunch_cost

print(total_cost)

# There are functions designed for lists
# len(): the number of items in a list
# max(): The biggest value in a list
# min(): The smallest value in a list

costs = [1.2, 4.3, 2.0, 0.5]
print(len(costs))
print(max(costs))
print(min(costs))

#Functions for changing the order of a list
#sorted(): Sorts the
#reversed(): Reverses the order of a list

costs = [1.2, 4.3, 2.0, 0.5]
print(sorted(costs))
print(list(reversed(costs)))

student_name = input('Which student are you looking for? ')
students = [
    'Diedre', 'Hank', 'Helena', 'Salome', # case sensitive
]
if student_name in students:
    print('{} is in the class'.format(student_name))
else:
    print('{} is not in the class'.format(student_name))

# The .append() method is used to add items to a list

students = [
'Diedre', 'Hank', 'Helena', 'Salome',
]
student_name = input('What is the name of the new student? ')
students.append(student_name)
print(students)

# Using lists and loops together

student_names = ['Diedre', 'Hank', 'Helena', 'Salome']
for student_name in student_names:
    print(student_name)


# Counting the total number of items in a list using a for loop

student_names = ['Diedre', 'Hank', 'Helena', 'Salome']
count = 0
for student_name in student_names:
    count = count + 1
print(count)

# Dictionary: stores a collection of labelled items. Each item has a key and a value

person = {
    'name': 'Jessica',
    'age': 23,
    'height': 172
}

print(person['name'])

place = {
    'name': 'The Anchor',
    'post_code': 'E14 6HY',
    'street_number': '54',
    'location': {
        'longitude': 127,
        'latitude': 63,
    }
}

print(place['name'])
print(place['post_code'])
print(place['street_number'])

# extension

print(place['location']['longitude'])
print(place['location']['latitude'])

# Or

location = place['location']

print(location['longitude'])
print(location['latitude'])

# Putting dictionaries inside a list

people = [
    {'name': 'Jessica', 'age': 23},
    {'name': 'Trisha', 'age': 24},
]
for person in people:
    print(person['name'])
    print(person['age'])


fruits = [
    {'name': 'apple', 'colour': 'red', 'price': 0.12},
    {'name': 'banana', 'colour': 'yellow', 'price': 0.2},
    {'name': 'pear', 'colour': 'green', 'price': 0.19},
]
for fruit in fruits:
    print(fruit['name'])
    print(fruit['colour'])
    print(fruit['price'])

# Random Choice
# The choice() function in the random module returns a random item from a list

import random
colours = ['red', 'green', 'blue']
chosen_colour = random.choice(colours)
print(chosen_colour)

