# Initial dictionary iteration example
hero01 = {
    'name': 'Moira',
    'role': 'support',
    'health': 200
}

# Iterate over the dictionary and print keys
for key in hero01:
    print(key)

# Iterate over the dictionary and print keys and values
for key in hero01:
    print(f'Key: {key}, Value: {hero01[key]}')

# Variation with incorrect key access (will cause an error)
hero02 = {
    'name': 'Moira',
    'role': 'support',
    'health': 200
}

# This will cause an error because 'key' is not a key in the dictionary
try:
    for key in hero02:
        print(f'Key: {key}, Value: {hero02["key"]}')
except KeyError as e:
    print(f"Error: {e}")

# Another example of iterating over a dictionary and accessing both keys and values
hero03 = {
    'name': 'Reinhardt',
    'role': 'tank',
    'health': 500
}

for key in hero03:
    print(f'Key: {key}, Value: {hero03[key]}')
