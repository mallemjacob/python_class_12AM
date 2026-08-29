# Loops - do something repeatedly


# if condition:
#   code block


# While loop

# while condition:
#     code block


# Print numbers from 1 to 10


# count = 1

# while count <= 100:  # 11 <= 10
#     print(count)  # 10
#     count = count + 1  # count = 11


# while True:
#     print('Enter your username:')
#     username = input()  # 'cat'

#     if username == 'mouse':  # 'cat' == 'mouse'
#         print('welcome')
#     else:
#         print('wrong username')


found = False
print('Enter your username:')
username = input()  # 'cat'

while username != 'mouse':  # 'mouse' != 'mouse'
    print('Wrong username')
    if not found:
        print('Enter your username:')
        username = input()  # 'mouse'


# Homework
correct_input = False
print('Enter your marks:')
student_marks = int(input())  # '10' --> student_marks = 10

if student_marks >= 1 and student_marks <= 35:
    print('You are failed.')
elif student_marks >= 36 and student_marks <= 50:
    print('Grade C')
elif student_marks >= 51 and student_marks <= 75:
    print('Grade B')
elif student_marks >= 75 and student_marks <= 100:
    print('Grade A')
else:
    print('Invalid marks')
