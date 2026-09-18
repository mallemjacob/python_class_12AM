# import time
# import sys

# Exception Handling or Error Handling


# try:
#   error excepting code
# except:
#   error handling code


# def divideBy(number):
#     try:
#         return 42 / number
#     except ZeroDivisionError:
#         print('Can not divide by zero')
#     except TypeError:
#         print('Only numbers are accepted.')


# print(divideBy(10))
# print(divideBy(0))
# print(divideBy('hi'))
# print(divideBy(4))
# print(divideBy(8))


# Collatz

# def collatz(number):  # number = 2
#     if number % 2 == 0:
#         print(number // 2)  # 1
#         return number // 2  # return 1
#     else:
#         print(3 * number + 1)
#         return 3 * number + 1


# while True:
#     try:
#         print('Enter a number: ')
#         user_input = int(input())  # user_input = 10

#         while True:
#             if user_input == 1:  # user_input = 1
#                 break
#             else:
#                 returned_value = collatz(user_input)  # colltaz(2) --> 1
#                 user_input = returned_value  # user_input = 1
#         break
#     except ValueError:
#         print('Only integers are accepted')


# None datatype

# def greet():
#     print('hi there')


# print(greet())


# Keyword arguments

# def greet(name, age):
#     return "Hi " + name + " Youre " + str(age) + ' years old.'


# print(greet(age=23, name='mouse'))

# end
# print('hi', end=' ')
# print('there')

# sep
# print("cat", "dog", "mouse", sep='*')

# print("cat", "dog", "mouse", sep='|')
# print("cat", "dog", "mouse", sep='      ')


# String concatenation

# print('hi ' + 'there')

# indentation
# if confiton:
#   code

# String replications

# print('*' * 8)
# print('********')
# print(' ', end='')
# print('********')
# print('  ', end='')
# print('********')

# ********
#  ********
#   ********
#    ********
#     ********
#      ********
#     ********
#    ********
#   ********
#  ********
# ********
#  ********
#   ********
#    ********
#     ********
#      ********


# Zigzag pattern

# indent = 0
# indentationIncrease = True


# try:
#     while True:
#         print(' ' * indent, end='')
#         print('********')
#         time.sleep(0.1)

#         if indentationIncrease:
#             indent = indent + 1
#             if indent == 10:
#                 indentationIncrease = False
#         else:
#             indent = indent - 1
#             if indent == 0:
#                 indentationIncrease = True
# except KeyboardInterrupt:
#     sys.exit()


# indent = 0
# indentationIncrease = True

# for i in range(100):
#     print(' ' * indent, end='')
#     print('*' * 8)
#     time.sleep(0.1)

#     if indentationIncrease:
#         indent = indent + 1
#         if indent == 10:
#             indentationIncrease = False
#     else:
#         indent = indent - 1
#         if indent == 0:
#             indentationIncrease = True

# Home work
# Add error handling to the zig-zap pattern program
# Import sys module
# sys.exit()

# try:
#   zigzag code
# except KeyboardInterrupt:
#   error ahndlign code


# kwargs
# def greet(**kwargs):
#     print(kwargs['name'])
#     print(kwargs['age'])
#     print(kwargs['language'])


# greet(name='mouse', age=23, language='French')
