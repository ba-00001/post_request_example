# WRITE YOUR CODE HERE


# test code below
# Dictionaries Exercise 4

def is_nested(d):
    """Return True if dictionary has a list, tuple, or dictionary as a value, else False."""
    for value in d.values():
        if isinstance(value, (list, tuple, dict)):
            return True
    return False

# 01 - Test Case 1
# Using the given dictionary and function call below:
if __name__ == "__main__":
    example_dict = {
        1: 'one',
        2: 'two',
        3: 'three'
    }
    print("Test Case 1")
    print(is_nested(example_dict))
    # Your script should print: False

# 02 - Test Case 2
# Using the given dictionary and function call below:
if __name__ == "__main__":
    example_dict = {
        1: (2, 3),
        4: 'four',
        5: 'five'
    }
    print("Test Case 2")
    print(is_nested(example_dict))
    # Your script should print: True

# 03 - Test Case 3
# Using the given dictionary and function call below:
if __name__ == "__main__":
    example_dict = {
        1: 'one',
        2: {3: 4},
        5: 'five'
    }
    print("Test Case 3")
    print(is_nested(example_dict))
    # Your script should print: True

# 04 - Test Case 4
# Using the given dictionary and function call below:
if __name__ == "__main__":
    example_dict = {
        1: 'one',
        2: 'two',
        3: [4, 5]
    }
    print("Test Case 4")
    print(is_nested(example_dict))
    # Your script should print: True

