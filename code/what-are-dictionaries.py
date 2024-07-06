# Initial Code Snippet
capitals01 = {
    'Canada': 'Ottawa',
    'France': 'Paris',
    'New Zealand': 'Wellington',
    'Argentina': 'Buenos Aires'
}

print(type(capitals01))

# Variation 1: Printing the dictionary
capitals02 = {
    'Canada': 'Ottawa',
    'France': 'Paris',
    'New Zealand': 'Wellington',
    'Argentina': 'Buenos Aires'
}

print(capitals02)

# Accessing Values
capitals03 = {
    'Canada': 'Ottawa',
    'France': 'Paris',
    'New Zealand': 'Wellington',
    'Argentina': 'Buenos Aires'
}

print(capitals03['Canada'])
print(capitals03['France'])
print(capitals03['New Zealand'])
print(capitals03['Argentina'])

# Error Examples
# Accessing with index (will cause an error)
capitals04 = {
    'Canada': 'Ottawa',
    'France': 'Paris',
    'New Zealand': 'Wellington',
    'Argentina': 'Buenos Aires'
}

# This will cause an error because dictionaries don't support indexing
try:
    print(capitals04[0])
except KeyError as e:
    print(f"Error: {e}")

# Slicing (will cause an error)
capitals05 = {
    'Canada': 'Ottawa',
    'France': 'Paris',
    'New Zealand': 'Wellington',
    'Argentina': 'Buenos Aires'
}

# This will cause an error because dictionaries don't support slicing
try:
    print(capitals05[:2])
except TypeError as e:
    print(f"Error: {e}")

# Declaring Dictionaries Incrementally
# Initial declaration and adding items
capitals06 = {}

capitals06['Canada'] = 'Ottawa'
capitals06['France'] = 'Paris'
capitals06['New Zealand'] = 'Wellington'
capitals06['Argentina'] = 'Buenos Aires'

print(capitals06)

# Accessing a non-existent key (will cause an error)
capitals07 = {}

# This will cause an error because 'Canada' key doesn't exist yet
try:
    print(capitals07['Canada'])
except KeyError as e:
    print(f"Error: {e}")

# Adding new items to an existing dictionary
capitals08 = {
    'Canada': 'Ottawa',
    'France': 'Paris',
    'New Zealand': 'Wellington',
    'Argentina': 'Buenos Aires'
}

capitals08['India'] = 'New Delhi'
print(capitals08)
