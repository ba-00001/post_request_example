# In Operator
# Like lists, the in operator returns a boolean if a key is found in a dictionary.

# Initial dictionary
watches_01 = {
    'Speedmaster': 'Omega',
    'Submariner': 'Rolex',
    'Tank': 'Cartier'
}

# Check if 'Tank' is a key in the dictionary
print('Tank' in watches_01)  # Output: True

# Check if 'Snowflake' is a key in the dictionary
print('Snowflake' in watches_01)  # Output: False

# Check if 'Omega' is in the dictionary
# Since 'Omega' is a value, not a key, this will return False
print('Omega' in watches_01)  # Output: False

# Check if a key is not in the dictionary
print('Calatrava' not in watches_01)  # Output: True

# Extract values and check if 'Omega' is a value in the dictionary
values_01 = watches_01.values()
print('Omega' in values_01)  # Output: True

# Check if the ('Tank', 'Cartier') pair is in the dictionary
items_01 = watches_01.items()
print(('Tank', 'Cartier') in items_01)  # Output: True

'''
# Inefficient way to search the dictionary
food = {
    'apple': 'fruit',
    'bell pepper': 'vegetable',
    'chickpea': 'legume'
}

keys = food.keys()
print('apple' in keys)  # Output: True

# More efficient way to search the dictionary
print('apple' in food)  # Output: True
'''
