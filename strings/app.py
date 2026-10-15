

# String literals
# name = 'mouse'

# greet = "welcome to my class "

# print(greet + name)


# 

# spam = 'That is Alice\'s cat.'


# Escape characters \'   \"   \t   \n   \\
  
  
# spam = "The committee couldn\'t decide who\'s going to lead the project, \n\t\t even though \"everyone\" knows whose [possessive without apostrophe] qualifications are the strongest"

# print(spam)



# print('Hi there')
# print('welcome')
# print('to my class')


# spam  = "Hi there\nwelcome\nto my class"


# spam  = r"C:\\ProgramFiles\\Users\\Videos"

# print(spam)


# # Raw Strings - unprocessed

# print(r'That is a Carol\'s cat')


# spam = '''  This is my multi string '''

# spam = """  This is my multi string """

# print(spam)

# # Doc strings
# '''
# This is a  multi line comment.
# This is a string methods class
# '''

# spam = ['cat','rat','bat']

# # print('dog' in spam)

# print('cat' not in spam)

# # are you in the class? yes or no
# # 'cat' in spam? True or False


# name = 'mouse'

# print('m' in name)
# print('z' in name)
# print('z' not in name)
# print('e' not in name)



# spam = "The committee couldn\'t decide who\'s going to lead the project, \n\t\t even though \"everyone\" knows whose [possessive without apostrophe] qualifications are the strongest"


# print("whose" in spam)


# # f-strings


# name = 'mouse'
# age = 5


# print('hi i am ' + name + ' i am ' + str(age)  + ' years old.')


# print(f'Hi i am {name} and i am {age} years old.')


# String methods

# upper()

# print('mouse'.upper())

# # isupper()
# print('mouse'.isupper())


# name = 'MOUSE'

# if not name.isupper():
#   name = name.upper()
# else:
#   print('Already in uppercase')

# print(name)

# lower(), islower()

# print('MOUSE'.lower())

# print('mouse'.islower())

# print('MOUSE'.islower())



# print('Enter your age: ')
# age = input() # '19'

# if age.isdecimal():
#   print('enter username:')
#   uname = input() # 'MOUSE'
  
#   if uname.lower() == 'mouse':
#     print('Enter your password. Must contain letters or numbers.')
#     pswd = input() 
#     if pswd.isalnum():
#       print('Welcome to the account')
#     else:
#       print('Wrong password')
#   else:
#     print('username doesnt exist')
# else:
#   print('Invalid age')

# # isalpha() - A-Z

# 'hi there'.isalpha()

# 'hithere'.isalpha()

# # isalnum()


# ' '.isalnum()
# # False
# ' hi there '.isalnum()
# # False
# 'hi'.isalnum()
# # True
# '123'.isalnum()
# # True
# 'password123'.isalnum()


# # isdecimal()
# 'hi'.isdecimal() # False
# '123'.isdecimal() # True


# # isspace()
# ' '.isspace() # True
# ' hihi'.isspace() # False


# # istitle()

# 'hi'.istitle() # False
# 'Hi'.istitle() # True
# 'HI'.istitle() # False


# # startswith(), 
# 'Hello, world!'.startswith('H') # True
# 'Hello, world!'.startswith('T') # False
# 'Hello, world!'.startswith('He') # True


# endswith()


files = ['app.py','python.pdf','index.py','backend.py','index.html','script.js','db.pdf','fastapi.py']

python_files = []

for i in files:
  if i.endswith('.py'):
    python_files.append(i)
    
print(python_files)


# mp3, mp4, png, jpeg, 


# when i login in
# bash - CORN job
# run app.py



# join()
','.join(['cats','rats','bats'])
# 'cats,rats,bats'

' | '.join(['cats','rats','bats'])
# 'cats | rats | bats'

# split()
'My name is mouse'.split()
# ['My', 'name', 'is', 'mouse']

'My*name*is mouse'.split()
# ['My*name*is', 'mouse']

'My*name*is mouse'.split('*')
# ['My', 'name', 'is mouse']



spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment."

Please do not drink it.
Sincerely,
Bob'''

print(spam.split('\n'))

# rjust()
'Hello'.rjust(10)
# '     Hello'

# ljust()
'Hello'.ljust(10, '*')
# 'Hello     '

# center()
'Hello'.center(10)
'  Hello   '



# 15-Oct-2026

# strip()

' hello    '.strip() # 'hello'

# rstrip()
' hello    '.rstrip() # ' hello'

# lstrip()
' hello    '.lstrip() # 'hello    '


