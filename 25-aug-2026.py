# If statement

# if condition:
#     code block


# if condition:
#   code block
# else:
#   code block

# if you are above 18, then you can come to my class, listen to my class, ask questions or else you can go to library, study python from basics.


# = assigning the value to the variable
# age = 18


# ==  comparing two values

# 'hi' == 'hi'


print('Hi there')
print('what is your name?')
student_name = input()  # mouse
print('Hi ' + student_name)

print('what is your age?')
age = int(input())  # age = 25

if age > 18:   # 25 > 18
    print('Welcome to my class')
    print('listen to my class')
    print('ask questions')
    print('what is your favourite subject?')
    fav_subject = input()  # fav_subject = python
    if fav_subject == 'python':  # python == python
        print('I too like python programming')
    else:
        print('I hate ' + fav_subject)
else:
    print('You can go to library.')
    print('study python from basics')


# Indentation - 4 spaces
