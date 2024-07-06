# Example 01: Using the get() method to safely access a value in a dictionary
def example_01():
    watches = {
        'Speedmaster': 'Omega',
        'Submariner': 'Rolex',
        'Tank': 'Cartier'
    }
    print(watches.get('Tank'))  # Output: Cartier

# Example 02: Using get() to provide a default message when a key is not found
def example_02():
    watches = {
        'Speedmaster': 'Omega',
        'Submariner': 'Rolex',
        'Tank': 'Cartier'
    }
    print(watches.get('Royal Oak'))  # Output: None

# Example 03: Using get() with a default value when a key is not found
def example_03():
    watches = {
        'Speedmaster': 'Omega',
        'Submariner': 'Rolex',
        'Tank': 'Cartier'
    }
    msg = 'The watch you are looking for does not exist'
    print(watches.get('Royal Oak', msg))  # Output: The watch you are looking for does not exist

# Example 04: Directly accessing a key that does not exist, causing a KeyError
def example_04():
    my_dict = {
        'blue': 'sky',
        'green': 'grass',
        'yellow': 'sun'
    }
    try:
        print(my_dict['red'])
    except KeyError:
        print("KeyError: 'red'")  # Output: KeyError: 'red'

# Example 05: Using get() with a different default value
def example_05():
    my_dict = {
        'blue': 'sky',
        'green': 'grass',
        'yellow': 'sun'
    }
    print(my_dict.get('red', 'Not found'))  # Output: Not found

# Run all examples
example_01()
example_02()
example_03()
example_04()
example_05()
