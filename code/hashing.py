# Hashing different data types
integer_hash_value01 = hash(749)
float_hash_value01 = hash(3.14)
string_hash_value01 = hash('hello world')
tuple_hash_value01 = hash(('blah', 42))

print(integer_hash_value01)
print(float_hash_value01)
print(string_hash_value01)
print(tuple_hash_value01)

# Hashing a user-defined object
class Example01:
    def __str__(self):
        return 'I am a user-defined object'

my_obj01 = Example01()
obj_hash_value01 = hash(my_obj01)

print(my_obj01)
print(obj_hash_value01)

# Dictionary key restrictions
# This will generate an error because lists are not hashable
try:
    my_list02 = [1, 2, 3, 4]
    my_dict02 = {my_list02: 'value'}
    print(my_dict02)
except TypeError as e:
    print(f"Error: {e}")

# This will generate an error because dictionaries are not hashable
try:
    dict_key03 = {'key': 'value'}
    my_dict03 = {dict_key03: 'value'}
    print(my_dict03)
except TypeError as e:
    print(f"Error: {e}")

# Tuples are hashable, so this will work
dict_key04 = ('key', 'value')
my_dict04 = {dict_key04: 'value'}
print(my_dict04)

# Hashing the same value produces the same output
str_105 = 'Hello world!'
str_205 = 'Hello world!'
print(hash(str_105) == hash(str_205))

# Unique keys in a dictionary
laptops06 = {
    'Dell': 'XPS',
    'Apple': 'MacBook Air',
    'Lenovo': 'ThinkPad'
}

laptops06['Apple'] = 'MacBook Pro'
print(laptops06)

# Case-sensitive keys in a dictionary
laptops07 = {
    'Dell': 'XPS',
    'Apple': 'MacBook Air',
    'Lenovo': 'ThinkPad'
}

laptops07['apple'] = 'MacBook Pro'
print(laptops07)
