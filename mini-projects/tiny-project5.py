#PIP & txt files

# Q1
# PIP stands for "Preferred Installer Program" and is used as a recommended tool to install additional libraries and
# packages that are not part of the standard Python library.

# benefits:
# - The latest version available can be installed but also target alternative versions of choice.
# - Can create a file text with a custom requirements package

# Q2
with open('poem.txt', 'w+') as poem_file:  # change the 'r' to 'w+' - from reading to writing
    poem = 'I like Python and I am not very good at poems'  # moved this line below for personal pref
    poem_file.write(poem)

poem = 'I like Python and I am not very good at poems'
with open('poem.txt', 'w+') as poem_file:   # change the 'r' to 'w+' - from reading to writing
    poem_file.write(poem)

# Q3
# get_pokemon.py
