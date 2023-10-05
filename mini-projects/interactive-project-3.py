# Q1 - if/else statements
rain = input("Is it raining? (y/n) ")
is_raining = rain == 'y'
if is_raining:
    print("Take an umbrella!")
else:
    print("you don't need an umbrella!")

# Q2
my_money = int(input("How much money do you have? "))  # added int to recognise the integers in the code
boat_cost = 20 + 5  # added the underscore to validate the syntax
if my_money >= boat_cost:
    # changed the position of the value and added an equals to ensure it's more than or equal to
    print('You can afford the boat hire')
else:
    print('You cannot afford the board hire')

# Q3
year = int(input("Find out the century and decade of the book by entering the year published: "))
if 1800 <= year <= 1899:
    century = "19th Century"
elif 1900 <= year <= 1950:
    century = "20th Century"
decade = year % 100
if 0 <= decade <= 9:
    decade_name = "Noughties"
elif 10 <= decade <= 19:
    decade_name = "10s"
elif 20 <= decade <= 29:
    decade_name = "20s"
elif 30 <= decade <= 39:
    decade_name = "30s"
elif 40 <= decade <= 49:
    decade_name = "40s"
elif 50 <= decade <= 59:
    decade_name = "50s"
elif 60 <= decade <= 69:
    decade_name = "60s"
elif 70 <= decade <= 79:
    decade_name = "70s"
elif 80 <= decade <= 89:
    decade_name = "80s"
elif 90 <= decade <= 99:
    decade_name = "90s"
print(f'{century}, {decade_name}')
