# Lists


name = 'mouse'
age = 23
PI = 3.14
alive = True


# fruits = ['apples', 'babanas', 'oranges', 'pears', 'strawberries']
# Indexes -- 0          1           2         3            4


# Total number of items in the list = 5
# Starting index = 0
# Last index = 4
# print(fruits)

# We can access list items using indexes
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])
# print(fruits[3])
# print(fruits[4])


# print(len(fruits))  # 5

# last_index = len(fruits) - 1  # 4

# print(fruits[last_index])


##########################################################
# List operations

# Accessing an item from list
# print(fruits[0])

##########################################################

# Updating an item from list

# print(fruits)

# fruits[0] = 'rat'
# fruits[1] = 'cat'
# fruits[2] = 'bat'
# fruits[3] = 'mouse'
# fruits[4] = 'elephant'

# print(fruits)
##########################################################

# Adding a new item to the list
#
# fruits = fruits + ['blackberries', 'blueberries']
# ['apples', 'babanas', 'oranges', 'pears', 'strawberries', 'blackberries']

# fruits = fruits + ['blueberries']

# print(fruits)


# # string concatnation
# print('hi' + 'there')

# # list concatnation
# print(['hi'] + ['there'])

# print(['cat', 'dog', 'rat'] + ['elephant'])


# aniamals = ['cat', 'dog', 'rat'] + ['mouse', 'snake', 'bee']


# print(aniamals)

##########################################################
# delete
# fruits = ['apples', 'babanas', 'oranges', 'pears', 'strawberries']

# print(fruits)

# del fruits[0]

# print(fruits)

##########################################################


# reverse indexexs

# reverse =     -5        -4         -3        -2         -1
# fruits = ['apples', 'babanas', 'oranges', 'pears', 'strawberries']
# indexes =   0           1          2         3          4


# -4 -3 -2 -1 0 1 2 3 4


# print(fruits[-1])
# print(fruits[-2])
# print(fruits[-3])
# print(fruits[-4])
# print(fruits[-5])


# Slicing

# list[starting:ending:step]
fruits = ['apples', 'babanas', 'oranges', 'pears', 'strawberries']

print(fruits[0:2])
print(fruits[0:len(fruits)])

print(fruits[::])

print(fruits[1:])

print(fruits[:4])


print(fruits[::-1])


print(fruits[::2])
print(fruits[::3])


# List replication
['a', 'b', 'c'] * 3
