# string formatting
cats = 10
cans = 2
total_cans = cats + cans

output = str(cats) + " cats eat " + str(total_cans) + " cans"  #strings
print(output)

animal = "cat"
description = "silly"
output = "{} {}".format(animal, description)  # {} are used to define a dictionary in a "list" called a literal. 
print(output)

# = this is how to make a comment that doesn't affect the code.

kids = input("How many kids in the class do you have?")
total_kids = int(kids) + 25
print(total_kids)

# input means you have to respond the answer in the running window (user interactive in console)
