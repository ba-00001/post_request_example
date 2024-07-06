# Initial example of iterating over a dictionary
heroes01 = {
    'Moira': 'support',
    'Sombra': 'dps',
    'Zarya': 'tank'
}

# Iterate over just the values
for value in heroes01.values():
    print(value)

# Another example with repeated values
heroes02 = {
    'Moira': 'support',
    'Sombra': 'dps',
    'Zarya': 'tank',
    'Ana': 'support'
}

for value in heroes02.values():
    print(value)

# Using the keys() method
heroes03 = {
    'Moira': 'support',
    'Sombra': 'dps',
    'Zarya': 'tank'
}

print('With the keys method:')
for key in heroes03.keys():
    print(f'\t{key} -> {type(key)}')

print('\nWithout the keys method:')
for key in heroes03:
    print(f'\t{key} -> {type(key)}')

# Accessing both key and value using different methods
# Method 1: Iterating over keys and accessing values
my_dict04 = {
    'red': 'primary color',
    'purple': 'NOT a primary color',
    'yellow': 'primary color'
}

for k in my_dict04:
    key = k
    value = my_dict04[k]
    print(f'Key: {key}, Value: {value}')

# Method 2: Iterating over items() to get both key and value
my_dict05 = {
    'blue': 'primary color',
    'green': 'secondary color',
    'orange': 'tertiary color'
}

for i in my_dict05.items():
    key = i[0]
    value = i[1]
    print(f'Key: {key}, Value: {value}')

# Example with incorrect key access in the loop
heroes06 = {
    'name': 'Moira',
    'role': 'support',
    'health': 200
}

try:
    for key in heroes06:
        print(f'Key: {key}, Value: {heroes06["key"]}')
except KeyError as e:
    print(f"Error: {e}")
