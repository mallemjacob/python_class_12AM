# Built in functions
# print()
# int()
# str()
# input()

# name = 'mouse'

# print('hi ' + name)

# User defined Functions

# code reuse
# scoped: code is isolated


# function definition

# def function_name(parameters):
#   function body

# function_name(arguments)


# def greet(day):  # day ---> parameter
#     # function body
#     print('welcome')
#     print('good ' + day)
#     print('Have a nice ' + day)


# # function calling
# greet('morning')  # 'morning' --- argument
# greet('afternoon')
# greet('evening')
# greet('night')


# def adder(num1, num2):  # num1 = 146352, num2 = 6848
#     print(num1 + num2)


# adder(1, 2)
# adder(146352, 6848)


# def adder(a, b, c):
#     print(a + b + c)


# adder(1, 2, 10)
# adder(1, 1, 1)
# adder(10, 11, 12)


# home
# create a calculator function, take 2 arguments, add, sub, divisdion, prnit the result on screen.


# def calculator(arg1, arg2):
#     print('The arg1 is ' + str(arg1))
#     print('The arg2 is ' + str(arg2))
#     print('Additon: ' + str(arg1 + arg2))
#     print('Subtraction: ' + str(arg1 - arg2))
#     print('Multiplication: ' + str(arg1 * arg2))
#     print('Division: ' + str(arg1 / arg2))


# print('Started Round 1')
# calculator(1, 2)  # fucntion calling
# print('Finished Round 1')
# print('-------------------------')
# print('Started Round 2')
# calculator(10, 5)  # fucntion calling
# print('Finished Round 2')


# # Home 1
# def greet():
#     # Local scope
#     name = "mouse"
#     print("Line 80: " + name)


# # Earth
# greet()

# # Global scope
# print("Line 84: " + name)

# # Home 2


# def welcome():
#     # local scope
#     print("Line 91: " + name)


# welcome()


# earth - -- 1 global scope

# home - -- local scope(function)


# return statement

def add(a, b):  # a = 10, b = 20
    total = a + b
    return total


returned_solution_1 = add(1, 2)
returned_solution_2 = add(10, 20)

print(returned_solution_1)
print(returned_solution_2)
