# catNames = []


# step 1: take user input --- input()
# step 2: store in the list
# check for duplicates

# while True:
#     print('Enter a cat name: ')
#     cat_name = input()  # cat_name = julie
#     if cat_name == '':  # cat_name == ''
#         break
#     elif cat_name in catNames:
#         print('Cat name already exists')
#     else:
#         catNames = catNames + [cat_name]

# print("The cat names are: ")
# for cat in catNames:
#     print(cat)


# lettes = ['a', 'b', 'c']
# for i in lettes:
#     print(i)


# in and not in operators
# 'elephant' in ['cat', 'dog', 'snake'] - -> False
# 'elephant' not in ['cat', 'dog', 'snake'] - -> True


# arthimetic = +, - *, /, // %  1+ 2
# comaprison = > < == != 1 > 2, 'hi' == 'hi'
# booelan = and or not 2 > 1 and 2 < 5
# string = +, * 'hi' * 3
# list = in, not in


fruits = ['apples', 'babanas', 'oranges', 'pears', 'strawberries', 'bb']
# indexes =   0           1          2         3          4          5

# for i in fruits:
#     print(i)
# i = 0
# fruits[i]


for i in range(len(fruits)):  # 0,1,2,3,4,5
    print(str(i) + " : " + fruits[i])
