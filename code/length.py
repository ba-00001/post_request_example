# Length Function
# Length

# Initial dictionary
watches_01 = {
  'Speedmaster': 'Omega',
  'Submariner': 'Rolex',
  'Tank': 'Cartier'
}

# Printing the length of the dictionary
print("Length of watches_01:", len(watches_01))

# TRY IT
# Variation 01: Change watches to be an empty dictionary.
watches_02 = {}
print("Length of watches_02:", len(watches_02))

# TRY IT
# Avoiding Errors with len
# Function to pop the last item from the dictionary
def pop_item_01(d):
    return d.popitem()

# Initial empty dictionary
watches_03 = {}
# This will cause an error
try:
    print("Pop item from watches_03:", pop_item_01(watches_03))
except KeyError as e:
    print("Error:", e)

# TRY IT
# Variation 02: Modified function to avoid errors by checking length
def pop_item_02(d):
    if len(d) == 0:
        return -1
    else:
        return d.popitem()

# Testing the modified function with an empty dictionary
print("Pop item from watches_03 with check:", pop_item_02(watches_03))

# TRY IT
