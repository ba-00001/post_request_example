# Deleting an Item using del statement
watches_01 = {
    'Speedmaster': 'Omega',
    'Submariner': 'Rolex',
    'Tank': 'Cartier'
}
del watches_01['Submariner']
print("After deleting 'Submariner' using del:")
print(watches_01)

# Try deleting an item that does not exist using del
watches_02 = {
    'Speedmaster': 'Omega',
    'Submariner': 'Rolex',
    'Tank': 'Cartier'
}
try:
    del watches_02['Royal Oak']
    print("After deleting 'Royal Oak' using del:")
    print(watches_02)
except KeyError as e:
    print(f"Error: {e}")

# Deleting Versus Popping
watches_03 = {
    'Speedmaster': 'Omega',
    'Submariner': 'Rolex',
    'Tank': 'Cartier'
}

# Attempting to delete using del statement
del watches_03['Speedmaster']
print("After deleting 'Speedmaster' using del:")
print(watches_03)

# Using pop() method to remove and return the value
watches_04 = {
    'Speedmaster': 'Omega',
    'Submariner': 'Rolex',
    'Tank': 'Cartier'
}
print("Using pop() method to remove and return 'Speedmaster':")
print(watches_04.pop('Speedmaster'))
print(watches_04)

# Using clear() method to empty the dictionary
watches_05 = {
    'Speedmaster': 'Omega',
    'Submariner': 'Rolex',
    'Tank': 'Cartier'
}
watches_05.clear()
print("After using clear() method:")
print(watches_05)

# Trying to use popitem() on an empty dictionary
watches_06 = {}
try:
    print("Trying to use popitem() on an empty dictionary:")
    print(watches_06.popitem())
except KeyError as e:
    print(f"Error: {e}")
