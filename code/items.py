# Initial example of iterating over a dictionary
colors01 = {
    'red': 'primary color',
    'purple': 'NOT a primary color',
    'yellow': 'primary color'
}

# Iterate over the dictionary and print keys and values
for key, value in colors01.items():
    print(key, value)

# Variation: Printing a formatted string with key and value
heroes02 = {
    'Moira': 'support',
    'Sombra': 'dps',
    'Zarya': 'tank'
}

for key, value in heroes02.items():
    print(f'{key} is a {value} hero.')

# Example of iterating over dictionary items and printing each item
heroes03 = {
    'Moira': 'support',
    'Sombra': 'dps',
    'Zarya': 'tank'
}

for item in heroes03.items():
    print(item)

# Another example of iterating and printing keys and values
colors04 = {
    'blue': 'primary color',
    'green': 'secondary color',
    'orange': 'tertiary color'
}

for key, value in colors04.items():
    print(key, value)
