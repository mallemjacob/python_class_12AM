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


import sys
import random
person = {
    'age': 23,
    'name': 'mouse',
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


# list_of_users = [
#     {'user_1': {
#         'name': 'mouse',
#         'age': 21,
#         'location': 'US',
#         'languages': ['fr', 'de']}
#      },

#     {'user_2': {
#         'name': 'cat',
#         'age': 22,
#         'location': 'France',
#         'languages': ['en', 'de']}
#      },

#     {'user_3': {
#         'name': 'bat',
#         'age': 23,
#         'location': 'Germany',
#         'languages': ['en', 'fr']}
#      }
# ]


# print(list_of_users[1]['user_2']['languages'][1])


# JSON - javascirpt object notation
# REST API - Application programming interface


# 3rd party import
# JSON
# API
# venv


# open browser --> https://github.com/search?q=python&type=repositories&s=stars&o=desc ---> shows the website


# python ---> https://api.github.com/search/repositories?q=language:python+sort:stars --> JSON data ---> convert to python dictionary

True
False


# open browser --> https://chatgpt.com/ ---> shows the website
# python ---> https://chatgpt.com/ ---> JSON data --> convert to python dictionary
# python ---> https://api.unsplash.com/ --> JSON data --> convert to python dictionary


# laptop --> project 1 --> python v2
#        --> prohect 2 --> python v3

#        chrome v45 --> fb, insgram
#        chrome v46 --> tiktok


# virtual environment

# laptop ---> fake environment(python v2 --> project1)
#        ----> fake environment (python v3 --> project 2 )


# laptop --> virtial environement (python project 1)
# virtial environement (python project 2)
# virtial environement (python project 3)
# virtial environement (python project 4)


# modules -- external pirce of code


# 1.build in modules
# 2.user defined modules
# 3.third party modules


# requests moduels --> we can do HTTP requests.


# https: // chatgpt.com/


# client --> server
# Browser ---> Python

# http --> websites
# GET - -> https: // chatgpt.com
# POST (username, password) --> https: // chatgpt.com
# PATCH (username, password) --> https: // chatgpt.com
# DELETE --> https: // chatgpt.com

# english --> humans to humans
# Give - -> bread
# Take - -> bread
# Adjust -> Add some more spices on my bread
# Remove - -> thorw it in trash


# login - - username, password


# python (requests) GET ---> https://chatgpt.com


# 1. Virtual environement
# 2. downlaod reqiest modules in that environement
# 3. Make HTTP request to a website
# 4. Website gives back JSON data
# 5. Convert to python dictionary


# Agentic AI --- LLM (chatgpt, gemini)
