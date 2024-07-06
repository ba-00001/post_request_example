# WRITE YOUR CODE HERE


# test code below
# Define the function to find the key for a given value
def find_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
    return None

# Test cases
if __name__ == "__main__":
    example_dict = {
        1: ['red', 'blue', 'green'],
        'Josh Jung': (9, 10),
        3: {0: 0},
        9000: 'impale mat a'
    }

    # Test Case 1
    key = find_key(example_dict, (9, 10))
    print(key)  # Expected output: Josh Jung

    # Test Case 2
    key = find_key(example_dict, {0: 0})
    print(key)  # Expected output: 3

    # Test Case 3
    key = find_key(example_dict, 'impale mat a')
    print(key)  # Expected output: 9000

