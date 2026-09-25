# Dictionary

# animals = ['cat', 'bat', 'rat']
# # --------  0       1      2


# print(animals[1])

# key(index) - -> value
# 0 - -> 'cat'
# 1 - -> 'bat'
# 2 - -> 'rat'

# [   ] --> list
# {   } ---> dictionary

# animals = {'cat': 'Maine Coon', 'bat': 'Big Brown Bat', 'rat': 'Dumbo'}

# key(any datatype) - -> value
# 'cat' - -> 'Maine Coon'
# 'bat' - -> 'Big Brown Bat'
# 'rat' - -> 'Dumbo'

# print(animals['cat'])
# print(animals['bat'])
# print(animals['rat'])


person = {
    'name': 'mouse',
    'age': 23,
    12345: 'passcode',
    True: 'alive'
}

# print(person['name'])
# print(person['age'])
# print(person[12345])
# print(person[True])


# 0: 'it means turn right'
# 1: 'it means make food spicy'


# 'go right': 'it means turn right'
# 'spicyfood': 'it means make food spicy'

# dictioanry methods


# print(person.keys())
# print('---------')
# print(person.values())
# print('---------')
# print(person.items())


# for i in person.keys():
#     print(i)

# print('-----------------')

# for j in person.values():
#     print(j)

# print('-----------------')

# for k in person.items():
#     print(k)


# Complex data structures.

# list of users

# user_1 - name, age, location, languages
# user_2 - name, age, location, languages
# user_3 - name, age, location, languages
# user_4 - name, age, location, languages
# user_5 - name, age, location, languages


list_of_users = [
    {'user_1': {
        'name': 'mouse',
        'age': 21,
        'location': 'US',
        'languages': ['fr', 'de']}
     },

    {'user_2': {
        'name': 'cat',
        'age': 22,
        'location': 'France',
        'languages': ['en', 'de']}
     },

    {'user_3': {
        'name': 'bat',
        'age': 23,
        'location': 'Germany',
        'languages': ['en', 'fr']}
     }
]


print(list_of_users[1]['user_2']['languages'][1])


# JSON - javascirpt object notation


# 3rd party import
# JSON
# API
# venv
