

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

print('MOUSE'.lower())

print('mouse'.islower())

print('MOUSE'.islower())



print('enter username:')
uname = input() # 'MOUSE'

if uname.lower() == 'mouse':
  print('Enter your password. Must contain letters or number.')
  pswd = input() 
  if pswd.isalnum():
    print('Welcome to the account')
  else:
    print('Wrong password')
else:
  print('username doesnt exist')


# isalpha()

'hi there'.isalpha()

'hithere'.isalpha()

# isalnum()


' '.isalnum()
# False
' hi there '.isalnum()
# False
'hi'.isalnum()
# True
'123'.isalnum()
# True
'password123'.isalnum()