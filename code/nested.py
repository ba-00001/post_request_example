# 01 - Basic nested dictionary
print("# 01 - Basic nested dictionary")
actor = {
  'first_name': 'Denzel',
  'last_name': 'Washington',
  'films': {
    'Malcolm X': 1992,
    'The Hurricane': 1999,
    'Training Day': 2001,
    'Fences': 2016
  }
}

print(actor)

# 02 - Nested dictionaries with lists and tuples
print("# 02 - Nested dictionaries with lists and tuples")
actor = {
  'first_name': 'Denzel',
  'last_name': 'Washington',
  'films': [
    ('Malcolm X', 1992),
    ('The Hurricane', 1999),
    ('Training Day', 2001),
    ('Fences', 2016)
  ],
  'oscars': [{
    'award': 'Best actor in a supporting role',
    'film': 'Glory',
    'year': 1990
  }, {
    'award': 'Best actor in a leading role',
    'film': 'Training Day',
    'year': 2002
  }]
}

print(actor)

# 03 - Pretty printing nested dictionary
print("# 03 - Pretty printing nested dictionary")
import pprint

actor = {
  'first_name': 'Denzel',
  'last_name': 'Washington',
  'films': [
    ('Malcolm X', 1992),
    ('The Hurricane', 1999),
    ('Training Day', 2001),
    ('Fences', 2016)
  ],
  'oscars': [{
    'award': 'Best actor in a supporting role',
    'film': 'Glory',
    'year': 1990
  }, {
    'award': 'Best actor in a leading role',
    'film': 'Training Day',
    'year': 2002
  }]
}

pprint.pprint(actor)

# 04 - Pretty printing nested dictionary with width 40
print("# 04 - Pretty printing nested dictionary with width 40")
import pprint

actor = {
  'first_name': 'Denzel',
  'last_name': 'Washington',
  'films': [
    ('Malcolm X', 1992),
    ('The Hurricane', 1999),
    ('Training Day', 2001),
    ('Fences', 2016)
  ],
  'oscars': [{
    'award': 'Best actor in a supporting role',
    'film': 'Glory',
    'year': 1990
  }, {
    'award': 'Best actor in a leading role',
    'film': 'Training Day',
    'year': 2002
  }]
}

pprint.pprint(actor, width=40)
