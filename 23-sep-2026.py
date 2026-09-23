# Sequence data type
# lists
# strings

# animal = 'cat'
# print("Line 6:", id(animal))

# print(animal)
# print(animal[0])
# print(animal[1])
# print(animal[2])


# animal[0] = 'b'
# print(animal)


# Mutable --> list
# Immutable --> string


# animal = 'b' + animal[1:]
# print(animal)
# print("Line 24:", id(animal))


# pets = ['cat', 'rat', 'bat']
# print(pets)
# print("Line 29:", id(pets))

# pets.append('elephant')
# print(pets)
# print("Line 33:", id(pets))


# pets = ['cat', 'rat', 'bat']
# print("Line 37:", id(pets))
# pets = ['cat', 'rat', 'bat'] + ['elephant']
# print("Line 39:", id(pets))


# Comma Code
# input
# spam = ['apples', 'bananas', 'tofu', 'cats', 'bats', 'bugs', 'moose']


# final_spam = ''

# for i in spam:
#     if spam.index(i) == len(spam) - 1:
#         final_spam = final_spam + 'and ' + i
#     else:
#         final_spam = final_spam + i + ', '

# print(final_spam)
# Output
# 'apples, bananas, tofu, cats, and bat'


# list in list

matrix = [['a', 'b'],
          ['c', 'd']]

# c,a --> a, c
# d,b

for i in range(len(matrix[0])):  # a,b
    row = ''
    for j in reversed(range(len(matrix))):
        row = row + matrix[j][i]

    print(row)

# print(matrix)
# print(matrix[0][0])
# print(matrix[0][1])
# print(matrix[1][0])
# print(matrix[1][1])


# for i in matrix:  # i = ['a', 'b']
#     for j in i:
#         print(i, j)

# Homework
# Character Picture Grid
# grid = [['.', '.', '.', '.', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['.', 'O', 'O', 'O', 'O', 'O'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['.', '.', '.', '.', '.', '.']]


# ..OO.OO..
# .OOOOOOO.
# .OOOOOOO.
# ..OOOOO..
# ...OOO...
# ....O....
