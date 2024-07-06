# Using pop() with an existing key
watches_01 = {
  'Speedmaster' : 'Omega',
  'Submariner' : 'Rolex',
  'Tank' : 'Cartier'
}

print(watches_01.pop('Submariner'))
print(watches_01)

# Using pop() with a non-existing key (causing an error)
watches_02 = {
  'Speedmaster' : 'Omega',
  'Submariner' : 'Rolex',
  'Tank' : 'Cartier'
}

try:
    print(watches_02.pop('Royal Oak'))
except KeyError as e:
    print(f"Error: {e}")

# Using pop() with a default value when the key is not found
watches_03 = {
  'Speedmaster' : 'Omega',
  'Submariner' : 'Rolex',
  'Tank' : 'Cartier'
}

print(watches_03.pop('Royal Oak', -1))

# Using popitem() to remove the last item
watches_04 = {
  'Speedmaster' : 'Omega',
  'Submariner' : 'Rolex',
  'Tank' : 'Cartier'
}

print(watches_04.popitem())
print(watches_04)

# Using popitem() on an empty dictionary (causing an error)
watches_05 = {}

try:
    print(watches_05.popitem())
except KeyError as e:
    print(f"Error: {e}")
