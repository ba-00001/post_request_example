# Copying and Comparison

# Copying a Dictionary
# If you use the assignment operator to make a copy of a dictionary, Python points to the same address in memory for both dictionaries. 
# That means a change to one dictionary is a change to the other.

# Variation 01: Using the assignment operator
watches1_01 = {
    'Speedmaster': 'Omega',
    'Submariner': 'Rolex',
    'Tank': 'Cartier'
}

watches2_01 = watches1_01
watches1_01['Submariner'] = 'Tudor'

print("Variation 01:")
print(watches1_01)
print(watches2_01)

# Variation 02: Using the copy() method
watches1_02 = {
    'Speedmaster': 'Omega',
    'Submariner': 'Rolex',
    'Tank': 'Cartier'
}

watches2_02 = watches1_02.copy()
watches1_02['Submariner'] = 'Tudor'

print("\nVariation 02:")
print(watches1_02)
print(watches2_02)

# Variation 03: Print the id (memory address) for each dictionary when using the assignment operator to copy and when using the copy() method.
watches1_03 = {
    'Speedmaster': 'Omega',
    'Submariner': 'Rolex',
    'Tank': 'Cartier'
}

print('\nVariation 03:')
print('No copy method')
print('--------------')

watches2_03 = watches1_03

print(id(watches1_03))
print(id(watches2_03))

print('\nWith copy method')
print('----------------')

watches2_03 = watches1_03.copy()

print(id(watches1_03))
print(id(watches2_03))

# Comparison Operators
# Python allows you to compare dictionaries with the equality operator (==). 
# It is important to note that two dictionaries are considered equal if they have the same key-value pairs. 
# Order is not important when making this comparison.

# Variation 04: Compare dictionaries with the equality operator (==)
watches1_04 = {
    'Speedmaster': 'Omega',
    'Submariner': 'Rolex',
    'Tank': 'Cartier'
}

watches2_04 = {
    'Tank': 'Cartier',
    'Submariner': 'Rolex',
    'Speedmaster': 'Omega'
}

print("\nVariation 04:")
print(watches1_04 == watches2_04)

# Variation 05: Compare dictionaries with the less than operator
watches1_05 = {
    'Speedmaster': 'Omega',
    'Submariner': 'Rolex',
    'Tank': 'Cartier'
}

watches2_05 = {
    'Tank': 'Cartier',
    'Submariner': 'Rolex',
    'Speedmaster': 'Omega'
}

print("\nVariation 05:")
try:
    print(watches1_05 < watches2_05)
except TypeError as e:
    print("Error:", e)

# Reading Question
# Assume the following dictionaries:
dict1 = {
    'cat': 'feline',
    'dog': 'canine',
    'wolf': 'canine',
    'tiger': 'feline'
}

dict2 = {
    'tiger': 'feline',
    'cat': 'feline',
    'Dog': 'canine',
    'wolf': 'canine',
}

dict3 = dict1.copy()

dict4 = {
    'tiger': 'feline',
    'cat': 'feline',
    'dog': 'canine',
    'wolf': 'canine',
}

# Which dictionaries would be considered equal using the comparison operator (==)? Hint, there is more than one correct answer.
# dict1 and dict3 are equal
# dict2 and dict4 are equal

print("\nReading Question:")
print(dict1 == dict3)
print(dict2 == dict4)
