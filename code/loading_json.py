# Reading JSON

# 01 - Reading JSON data from file and creating a dictionary

import json

# Attempt to open the JSON file and load its contents into a dictionary
try:
    with open('example.json') as file:
        info = json.load(file)
    print("Case Example: Loading JSON file into a dictionary")
    print(type(info))
except FileNotFoundError:
    print("Error: The file 'example.json' was not found.")

# 02 - Print the name of the band from the JSON data

try:
    with open('data/music.json') as music_json:
        music_data = json.load(music_json)
    print("Case Example: Print the name of the band")
    print(music_data['name'])
except FileNotFoundError:
    print("Error: The file 'data/music.json' was not found.")

# 03 - Print the name of the area where the band begun

try:
    with open('data/music.json') as music_json:
        music_data = json.load(music_json)
    print("Case Example: Print the name of the area where the band begun")
    print(music_data['begin-area']['name'])
except FileNotFoundError:
    print("Error: The file 'data/music.json' was not found.")

# 04 - Pretty print JSON data with an indentation of 1

try:
    with open('data/music.json') as music_json:
        music_data = json.load(music_json)
    print("Case Example: Pretty print JSON data with an indentation of 1")
    print(json.dumps(music_data, indent=1))
except FileNotFoundError:
    print("Error: The file 'data/music.json' was not found.")

# 05 - Pretty print JSON data with an indentation of 3

try:
    with open('data/music.json') as music_json:
        music_data = json.load(music_json)
    print("Case Example: Pretty print JSON data with an indentation of 3")
    print(json.dumps(music_data, indent=3))
except FileNotFoundError:
    print("Error: The file 'data/music.json' was not found.")
