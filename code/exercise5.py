# WRITE YOUR CODE HERE


# test code below
# 01 - JSON Exercise
# Create the function compare which takes two file paths. 
# The function opens each JSON file and returns a string stating:
# The dictionaries are equal
# Dictionary 1 has more items than dictionary 2
# Dictionary 2 has more items than dictionary 1
# Dictionary 1 and Dictionary 2 have the same number of items

import json

def compare(f1, f2):
    with open(f1) as file1, open(f2) as file2:
        data1 = json.load(file1)
        data2 = json.load(file2)
        
        if data1 == data2:
            return 'The dictionaries are equal'
        else:
            count1 = len(data1)
            count2 = len(data2)
            if count1 > count2:
                return 'Dictionary 1 has more items than dictionary 2'
            elif count2 > count1:
                return 'Dictionary 2 has more items than dictionary 1'
            else:
                return 'Dictionary 1 and Dictionary 2 have the same number of items'

# Test code below
if __name__ == "__main__":
    import sys
    
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    
    print("Case Example: Compare two JSON files")
    print(compare(file1, file2))

# Test Case 1
# Using the given JSON files and function call below:
# file1: bored.json
# file2: coin_desk.json
# Expected Output: Dictionary 1 has more items than dictionary 2

# Test Case 2
# Using the given JSON files and function call below:
# file1: bored.json
# file2: bored.json
# Expected Output: The dictionaries are equal

# Test Case 3
# Using the given JSON files and function call below:
# file1: user.json
# file2: weather.json
# Expected Output: Dictionary 2 has more items than dictionary 1

# Test Case 4
# Using the given JSON files and function call below:
# file1: bored2.json
# file2: bored.json
# Expected Output: Dictionary 1 and Dictionary 2 have the same number of items

# Instructions:
# To test this script, use the command line to run the script with the file paths as arguments.
# Example: python script.py file1.json file2.json