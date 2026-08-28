# multiple conditions

# 75 - 100 grade A
# 51 - 75 grade B
# 36 - 50 grade C
# 1 - 35 Fail


# if condition:
#     code block
# elif condition:
#     code block
# else:
#     code block

# top
# |
# |
# |
# Bottom


print('Enter your marks:')
student_marks = int(input())  # '10' --> student_marks = 10

if student_marks >= 1 and student_marks <= 35:
    print('You are failed.')
elif student_marks >= 36 and student_marks <= 50:
    print('Grade C')
elif student_marks >= 51 and student_marks <= 75:
    print('Grade B')
    student_marks = 50
elif student_marks >= 75 and student_marks <= 100:
    print('Grade A')
else:
    print('Invalid marks')


print(student_marks)


# Variables

# =  assignment operator


# Creating a new variable
age = 10

print(age)

age > 11  # 10 > 11 --> False

age = 11

# Updating the variable
age = age + 1  # age = 12

age = age + 1  # age = 13

age = age + 1
age = age + 1
age = age + 1
age = age + 1
