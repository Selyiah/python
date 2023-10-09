# Comparison & Logical Operators
# Boolean is a data-type that is either true or false
# Comparison operator: compares values to determine whether something is true or false

today = input("what day is it?")
is_monday = today == "Monday"
print("today is Monday: {}" .format(is_monday))

#input interacts with the user

#float function convert solid number to decimal number

temperature = input("what is the temperature?")
is_freezing = float(temperature) <= 0.0
print("The temperature is freezing: {}" .format(is_freezing))

price = input("what is the price of the burger?")
within_budget = float(price) <= 10.00
print("The Burger is within budget: {}" .format(within_budget))

# so no decimals when it's an integer as it will produce an error, only decimal inputs when the result is float.

# Name Python
# Equal to ==
# Not equal !=
# Greater than >
# Less than <
# Greater than or equal >=
# Less than or equal <=

#There are logical operators to combine multiple checks

#Python What it does
#and = both expressions are True
#or = at least one expression is True
#not = reverse the expression (True becomes False and vice-versa)

#boolean
mars_choice = input("Would you like to visit Mars? y/n ")
is_willing = mars_choice == "y"
# == sign is a comparison operator to check that two values are equal
affordable = input("Can you afford to visit mars? y/n ")
can_afford = affordable == "y"
should_visit_mars = is_willing and can_afford
print("You should visit Mars: {}".format(should_visit_mars))


burger_choice = input("is there a vegetarian burger option? y/n ")
is_available = burger_choice == "y"
within_budget = input("can you afford the vegetarian burger? y/n ")
in_budget = within_budget == "y"
buy_vegetarian_burger = is_available and in_budget
print("You should buy the vegetarian burger: {}".format(buy_vegetarian_burger))


price = input("how much is a burger? ")
vegetarian = input("Is there a vegetarian option? y/n ")
within_budget = float(price) <= 10.00
has_vegetarian = vegetarian == "y"
is_good_choice = within_budget and has_vegetarian
print("Restaurant meets criteria: {}".format(is_good_choice))

#if statement
name = input("what is your name? ")
is_admin = name == "admin"
password = input("what is your password? ")
is_password_correct = password == "dinosaurs"
if is_admin and is_password_correct:
    print("Welcome")
if not is_admin or not is_password_correct:
    print("Go away")


restaurant = input("Is this restaurant a good choice? y/n ")
good_choice = restaurant == "y"
if good_choice:
    print("This restaurant is a great choice!")
if not good_choice:
    print("Probably not a good idea")

