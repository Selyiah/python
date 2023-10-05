# Q1

shopping_list = [
    "oranges",
    "cat food",
    "sponge cake",
    "long-grain rice",
    "cheese board",
]
print(shopping_list[0])  # changed the numeric to 0 to start from the top as it would range from 0-4 in a 5 item list

# Q2
chocolates = {
    ' white': 1.50,
    ' milk': 1.20,
    ' dark': 1.80,
    ' vegan': 2.00,
}
item = input("which chocolate flavour would you like?")
print(chocolates[item])

# Q3

import random

lottery_ticket = [5, 9, 27, 54, 38, 15, 7]
print("lottery ticket:", lottery_ticket)
lottery_numbers: list[int] = []
for number in range(7):
    random_numbers = random.randint(1, 60)
    lottery_numbers.append(random_numbers)
print("Lottery numbers:", lottery_numbers)
num_matches = 0
for number in lottery_ticket:
    if number in lottery_numbers:
        num_matches += 1
prize = 0
if num_matches == 3:
    prize = 20
elif num_matches == 4:
    prize = 40
elif num_matches == 5:
    prize = 100
elif num_matches == 6:
    prize = 10000
elif num_matches == 7:
    prize = 1000000
else:
    prize = 0
if prize == 0:
    print("None of your numbers matched! Sorry you're out")
else:
    print(f"Congratulations! You numbers matched by: {num_matches}  "
          f"You win £{prize}")
