# The Collatz Sequence


# Write a function named collatz() that has one parameter named number.

# If number is even, then collatz() should print number // 2 and return this value.

# If number is odd, then collatz() should print and return 3 * number + 1.

# Then write a program that lets the user type in an integer

# and that keeps calling collatz() on that number until the function returns the value 1.


# function definition
def collatz(number):  # number = 2
    if number % 2 == 0:
        print(number // 2)  # 1
        return number // 2  # return 1
    else:
        print(3 * number + 1)
        return 3 * number + 1


print('Enter a number: ')

user_input = int(input())  # user_input = 10

while True:
    if user_input == 1:  # user_input = 1
        break
    else:
        returned_value = collatz(user_input)  # colltaz(2) --> 1
        user_input = returned_value  # user_input = 1


# Keep looping (keep calling collatz function until 1)
#   collatz(10) --> 5
#   collatz(5) --> 16
#   collatz(16) --> 8
#   collatz(8) --> 4
#   collatz(4) --> 2
#   collatz(2) --> 1


# i = input()

# i = 10


# name = 'mouse'

# name = 'cat'


# i = 0

# while i < 10:  # 3 < 10
#     print(i)  # 2
#     i = i + 1  # i = 3
