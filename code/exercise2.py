# WRITE YOUR CODE HERE


# test code below
def move_to_bottom(d, key):
    """
    Moves the specified key to the bottom of the dictionary.
    If the key is not in the dictionary, returns a message.
    """
    if key not in d:
        return "The key is not in the dictionary"
    
    # Get the value associated with the key
    value = d[key]
    
    # Delete the key-value pair from the dictionary
    del d[key]
    
    # Add the key-value pair to the dictionary, moving it to the bottom
    d[key] = value
    
    return d

# Test Case 1
if __name__ == "__main__":
    # Test with key 1
    example_dict_01 = {
        1: 'one',
        2: 'two',
        3: 'three'
    }
    print("Test Case 1")
    result_01 = move_to_bottom(example_dict_01, 1)
    print(result_01)  # Expected: {2: 'two', 3: 'three', 1: 'one'}

    # Test with key 2
    example_dict_02 = {
        1: 'one',
        2: 'two',
        3: 'three'
    }
    print("Test Case 2")
    result_02 = move_to_bottom(example_dict_02, 2)
    print(result_02)  # Expected: {1: 'one', 3: 'three', 2: 'two'}

    # Test with key not in the dictionary
    example_dict_03 = {
        1: 'one',
        2: 'two',
        3: 'three'
    }
    print("Test Case 3")
    result_03 = move_to_bottom(example_dict_03, 4)
    print(result_03)  # Expected: The key is not in the dictionary

