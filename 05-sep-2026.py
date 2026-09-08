# continue


# break - exits out of a loop
# continue - skips a loop


# Break
# for i in range(1, 11):  # 1,2,3,4,5,6,7,8,9,10
#     if i == 5:  # 5 == 5
#         break
#     else:
#         print(i)


# print('The end')


# Continue
# for i in range(1, 11):  # 1,2,3,4,5,6,7,8,9,10
#     if i >= 3 and i <= 6:  # 6 == 5
#         continue
#     else:
#         print(i)


# range arguments


# for i in range(1, 11, 3):  # 1,2,3,4,5,6,7,8,9,10
#     print(i)


# A Short Program: Guess the Number

# I am thinking of a number between 1 and 20.
# Take a guess.
# 5
# Your guess is too low.
# Take a guess.
# 7
# Your guess is too low.
# Take a guess.
# 12
# Your guess is too high.
# Take a guess.
# 11
# Your guess is too high.
# Take a guess.
# 10
# Good job! You guessed my number in 4 guesses!


# for loop
# if statements
# comparison operators
# random number generator


# python modules - external piece of code


import random

print('I am thinking of a number between 1 and 20.')
random_number = random.randint(1, 20)  # 17

while True:
    print('Take a guess.')
    user_input = int(input())  # 17

    if user_input < random_number:
        print('Your guess is too low.')
    elif user_input > random_number:  # 19 > random_number
        print('Your guess is too high.')
    elif user_input == random_number:
        print('Good job! You guessed my number correctly!')
        break
