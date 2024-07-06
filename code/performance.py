# Performance Benefits
# Lists versus Dictionaries
# Over the course of these assignments, you have probably noticed similarities and differences between dictionaries and lists. One difference that has not been obvious is the performance advantage of dictionaries.
# The script below times how long it takes to run the test_list() and test_dict() functions. There is also a list with the elements 0 to 199 and a dictionary that has keys 0 to 199 and values 0 to 199. Each function runs a for loop 200 times. The test_list() function asks if each number from the loop is an element in the list. The test_dict() function asks if each number from the loop is a key in the dictionary.

import timeit
import sys

num = int(sys.argv[1])  # Number of elements in list/dict
large_list = [i for i in range(num)]  # Creating a list of length num
large_dict = dict(zip(large_list, large_list))  # Creating a dictionary with keys and values from large_list

def test_dict():
    # Check if each number in range(num) is a key in large_dict
    for i in range(num):
        i in large_dict

def test_list():
    # Check if each number in range(num) is an element in large_list
    for i in range(num):
        i in large_list

list_time = timeit.timeit(test_list)  # Timing the list test
dict_time = timeit.timeit(test_dict)  # Timing the dictionary test

print(f'List time: {list_time}')  # Print the time taken for list test
print(f'Dictionary time: {dict_time}')  # Print the time taken for dictionary test

# Try these variations:

# 01 Run the same test again, but use a list and dictionary with the length of 10 instead of 200.
# Command to run: python3 code/performance.py 10

# 02 Pass the script a much larger number than 200.
# Command to run: python3 code/performance.py 500

# Why are Dictionaries Faster?
# The performance advantage of dictionaries goes back to one of their defining characteristics, hashing.
# A dictionary is not stored in memory just like it is written in code. The order of items is determined by the hashed value of the key. More importantly, there can be “gaps” between items because the hashed value of their keys can be very different from one another.

# When you type 'seven' in my_dict, you are hashing the string 'seven' and looking directly for this value in the dictionary.
# Now compare that to how a list works. There are no hashed values, and the elements are stored in adjacent memory.
# Typing 'seven' in my_list means Python goes through each element and checks if it is 'seven'.
# This is why dictionaries are so much faster.

# Reading Question
# Fill in the blanks below.

# The performance of a list is proportional to its length.
# The performance of a dictionary is independent of its length.
