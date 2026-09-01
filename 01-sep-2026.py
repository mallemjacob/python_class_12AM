# break - stops the loop


# while True:
#     print('Enter your username:')
#     username = input()  # 'mouse'
#     if username == 'mouse':
#         print('Welcome Mouse')
#         break
#     else:
#         print('Wrong username try again.')


# nested while loop


# while condition:
#     while condition:
#         break
#     break


# if you want to check something - -> use if
# if you want to repeat something - -> use loops


# while True:
#     print('Enter your username:')
#     username = input()  # 'mouse'
#     if username == 'mouse':
#         print('Welcome Mouse')
#         while True:
#             print('Enter your password')
#             password = input()  # 'swordfish'
#             if password == 'swordfish':
#                 print('Welcome to your account')
#                 break
#             else:
#                 print('Wrong password')
#         break
#     else:
#         print('Wrong username try again.')


# while - run until condition is false.
# for  - run specific number of times.

# while condition:
#   code block

# for i in range(number):
#   code block


# for i in range(1, 11):  # 1,2,3,4,5,6,7,8,9,10
#     print(i)


# for i in range(15, 20):  # 1,2,3,4,5,6,7,8,9,10
#     print(i)


for i in range(3):  # 0,1,2
    print(i)


while True:
    print('Enter your username:')
    username = input()  # 'mouse'
    if username == 'mouse':
        print('Welcome Mouse')
        for i in range(1, 4):  # 1, 2, 3
            print('Enter your password')
            password = input()  # 'black'
            if password == 'swordfish':
                print('Welcome to your account')
                break
            else:
                print('Wrong password')
                print('You have ' + str(3 - i) + ' attempts left')
        break
    else:
        print('Wrong username try again.')
