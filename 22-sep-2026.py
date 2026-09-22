# enumerate

# fruits = ['apples', 'babanas', 'oranges',
#           'pears', 'strawberries', 'blackberries']
# indexes =   0           1          2         3          4          5

# for index, item in enumerate(fruits):
#     print(index, item)


# The Multiple Assignment Trick

# import random
# name = 'mouse'
# age = 20

# cat = ['fat', 'gray', 'loud']

# cat_size = cat[0]
# cat_color = cat[1]
# cat_disposition = cat[2]

# size, color, disposition = ['fat', 'gray', 'loud']

# print(size)
# print(color)
# print(disposition)


# modules

# pets = ['Dog', 'Cat', 'Moose']

# print(random.choice(pets))

# random.shuffle(pets)

# print(pets)


# Methods

# data type -> interger, floats, string, boolean, list
# functions -> print(), input(), len()


# List methods

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list ( or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

# pets = ['Dog', 'Cat', 'Moose']
# print(pets)

# # append()
# # pets = pets + ['Bat']
# pets.append('Bat')
# print(pets)

# clear()

# pets.clear()
# print(pets)


# copy()

# new_pets = pets.copy()

# print(new_pets)


# alphanets = ['a', 'b', 'c', 'd', 'e', 'a', 'c', 'a']
# print(alphanets.count('z'))


# alphanets.extend(['x', 'y', 'z'])
# print(alphanets)


# fruits = ['apples', 'babanas', 'oranges', 'pears', 'strawberries']

# print(fruits.index('pears'))

# # if 'banana' in fruits:
# #     print(fruits.index('babana'))
# # else:
# #     print('No banana')


# fruits.insert(1, 'Guava')

# print(fruits)

# fruits.pop(2)
# print(fruits)


# fruits.remove('Guava')
# print(fruits)


# reverse()

fruits = ['apples', 'babanas', 'oranges', 'pears', 'cherries', 'strawberries']

# print(fruits[::-1])

# fruits.reverse()
# print(fruits)


fruits.sort()

print(fruits)
