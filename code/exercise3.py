# WRITE YOUR CODE HERE


# test code below
# Define the function swap which takes a dictionary and swaps its keys and values
def swap(d):
    try:
        # Attempt to swap keys and values
        return {v: k for k, v in d.items()}
    except TypeError:
        # Return an error message if a value is unhashable
        return "Cannot swap the keys and values for this dictionary"

# Test Case 01
# Using the given dictionary and function call below:
if __name__ == "__main__":
    example_dict_01 = {
        1: 'one',
        2: 'two',
        3: 'three'
    }
    swapped_01 = swap(example_dict_01)
    print(swapped_01)
    # Expected Output: {'one': 1, 'two': 2, 'three': 3}

# Test Case 02
# Using the given dictionary and function call below:
if __name__ == "__main__":
    example_dict_02 = {
        1: [2, 3],
        4: 'four',
        5: 'five'
    }
    swapped_02 = swap(example_dict_02)
    print(swapped_02)
    # Expected Output: Cannot swap the keys and values for this dictionary

# Test Case 03
# Using the given dictionary and function call below:
if __name__ == "__main__":
    example_dict_03 = {
        1: 'one',
        2: {3: 4},
        5: 'five'
    }
    swapped_03 = swap(example_dict_03)
    print(swapped_03)
    # Expected Output: Cannot swap the keys and values for this dictionary

# Test Case 04
# Using the given dictionary and function call below:
if __name__ == "__main__":
    example_dict_04 = {
        1: 'one',
        2: 'two',
        3: (4, 5)
    }
    swapped_04 = swap(example_dict_04)
    print(swapped_04)
    # Expected Output: {'one': 1, 'two': 2, (4, 5): 3}

