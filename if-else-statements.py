#if/else statements
password = input('password: ')
if password == 'jumanji':
    print('Success!')
else:
    print('Failure!')

name = input("What is your name? ")
is_admin = name == 'admin'
password = input("What is your password? ")
is_password_correct = password == 'dinosaurs'
if is_admin and is_password_correct:
    print('Welcome')
else:
    print('Go away')


meal_price = float(input('How much did the meal cost? '))
discount_choice = input('Do you have a discount? y/n ')
is_discount = discount_choice == 'y'
is_over_twenty = meal_price >= 20.0
discount_applicable = is_discount and is_over_twenty
if discount_applicable:
    meal_price = meal_price * 0.9
    print('Discount applied')
else:
    print('No discount')

print('Total cost: {}'.format(meal_price))


dog_size = int(input('How big is the dog? '))

if dog_size > 75:
    print('That is a big dog')

elif dog_size < 10:
    print('That dog could fit in my pocket')

elif dog_size < 25:
    print('That is a small dog')

else:
    print('That is an average dog')


temperature = float(input('What is the temperature of the oven? '))
if temperature > 200:
    print('The oven is too hot')
elif temperature < 150:
    print('The oven is too cold')
elif temperature == 180:
    print('The oven is at the perfect temperature')
else:
    print('The temperature is close enough')

