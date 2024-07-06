# Updating and Creating
# Variation 01: Updating values in a dictionary
watches_01 = {
    'Speedmaster': 'Omega',
    'Submariner': 'Rolex',
    'Tank': 'Cartier'
}
watches_01.update(Speedmaster='Swatch Group', Tank='Richemont')
print(watches_01)

# Variation 02: Combining one dictionary with another dictionary
watches1_02 = {
    'Speedmaster': 'Omega',
    'Submariner': 'Rolex',
    'Tank': 'Cartier'
}
watches2_02 = {
    'Calatrava': 'Patek Philippe',
    'Datejust': 'Rolex',
    'Royal Oak': 'Audemars Piguet'
}
watches1_02.update(watches2_02)
print(watches1_02)

# Variation 03: Combining a dictionary with a list of tuples
watches1_03 = {
    'Speedmaster': 'Omega',
    'Submariner': 'Rolex',
    'Tank': 'Cartier'
}
watches2_03 = [
    ('Calatrava', 'Patek Philippe'),
    ('Datejust', 'Rolex'),
    ('Royal Oak', 'Audemars Piguet')
]
watches1_03.update(watches2_03)
print(watches1_03)

# Variation 04: Combining a dictionary with a list of lists
watches1_04 = {
    'Speedmaster': 'Omega',
    'Submariner': 'Rolex',
    'Tank': 'Cartier'
}
watches2_04 = [
    ['Calatrava', 'Patek Philippe'],
    ['Datejust', 'Rolex'],
    ['Royal Oak', 'Audemars Piguet']
]
watches1_04.update(watches2_04)
print(watches1_04)

# Variation 05: Using fromkeys() with a list
models_05 = ['Speedmaster', 'Submariner', 'Tank']
watches1_05 = dict.fromkeys(models_05)
watches2_05 = dict.fromkeys(models_05, 'Manufacturer')
print(watches1_05)
print(watches2_05)

# Variation 06: Using fromkeys() with a tuple
models_06 = ('Speedmaster', 'Submariner', 'Tank')
watches_06 = dict.fromkeys(models_06)
print(watches_06)

# Variation 07: Using fromkeys() with an empty dictionary
models_07 = ['Speedmaster', 'Submariner', 'Tank']
watches_07 = {}.fromkeys(models_07)
print(watches_07)
