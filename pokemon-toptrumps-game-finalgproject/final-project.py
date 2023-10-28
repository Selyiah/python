import random
import requests
import csv


def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number) # pokemon API
    response = requests.get(url)
    pokemon = response.json()
    return {
        'name': pokemon['name'],
        'forms': ', '.join([form['name'] for form in pokemon['forms']]),
        'abilities': ', '.join([ability['ability']['name'] for ability in pokemon['abilities']]),
        'height': pokemon['height'],
        'base_experience': pokemon['base_experience'],
        'weight': pokemon['weight'],
    }


def battle_round(round_number: object, display_key: object) -> object:
    print("{} ROUND".format(round_number))

    my_pokemon = random_pokemon()
    print('You were given {}: {}'.format(display_key, my_pokemon[display_key]))

    valid_choices = ['height', 'weight', 'base_experience'] # stats we used to fight with in the game as they are qunatifiable 
    while True:
        stat_choice = input('Which stat do you want to use? (height, weight, base_experience) ')
        if stat_choice in valid_choices:
            break
        print("Invalid choice! Please choose one of the valid options.")

    opponent_pokemon = random_pokemon()
    print('The opponent chose {}: {}'.format(display_key, opponent_pokemon[display_key]))

    my_stat = my_pokemon[stat_choice]
    opponent_stat = opponent_pokemon[stat_choice]
    if my_stat > opponent_stat:
        output = " player won "
        print('You Win!')

    elif my_stat < opponent_stat:
        output = " Computer won "
        print('You Lose!')


    else:
        print('Draw!')
        output = "Draw!"
        print('Draw!')

    return output


def write_to_csv(output, output1):
    field_names = ['FIRST ROUND', 'SECOND ROUND']  # Headers

    data = [
        {'FIRST ROUND': output, 'SECOND ROUND': output1},  # {Key col1 (round1):value , key col2 (round2): value} ---> row1 #
    ]

    with open('recordscores.csv', 'w+') as csv_file:
        spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)  # DictWriter is a class

        spreadsheet.writeheader()  # this will write the headers into the csv file
        spreadsheet.writerows(data)  # this will write the rows into the csv file


def run():
    output= battle_round("FIRST", "abilities") # abilities & forms where plays we used alternatively from 'name' which was found in the pokemon API 

    output1 = battle_round("SECOND", "forms")
    write_to_csv(output, output1)

if __name__ == '__main__':
    run()
