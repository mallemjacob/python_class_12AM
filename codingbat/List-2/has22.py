
# Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.


def has22(nums):
  
  for i in range(len(nums) - 2):  # len(3) - 2 = 1
    if nums[i] == 2 and nums[i + 1] == 2 and nums[i + 2]:
      return True
  
  return False


print(has22([1, 2, 2])) # True   range(2) --> 0, 1, 2
print(has22([1, 2, 1, 2])) # False
print(has22([2, 1, 2])) # False



# i = 4, i = 5
for i in range(1,6): # 1,2,3,4,5
  print(i)
  
# round 1  
# 1,2

# round 2
# 2,3

# round 3
# 3,4

# round 4
# 4,5


# round 1  
# 1

# round 2
# 2

# round 3
# 3

# round 4
# 4

# round 5
# 5

for  i in range(5):  # range(5) --> 0,1,2,3,4