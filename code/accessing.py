# 01 - Accessing nested values
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

print("01 - Accessing first film's name:")
movie = actor['films'][0][0]
pprint.pprint(movie)

print("\n02 - Accessing the last name:")
last_name = actor['last_name']
pprint.pprint(last_name)

print("\n03 - Accessing the film 'Glory':")
glory_film = actor['oscars'][0]['film']
pprint.pprint(glory_film)

print("\n04 - Keys, values, and items:")
pprint.pprint(actor.items())

print("\n05 - Printing a list of items:")
pprint.pprint(list(actor.items()))

print("\n06 - Printing keys for all Oscar dictionaries:")
oscars = actor['oscars']
for oscar in oscars:
  pprint.pprint(oscar.keys())
