
# Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.

def sum13(nums):
  sum = 0
  i = 0
  
  while i < len(nums): # 7 < 7
    if nums[i] == 13: # 1 == 13
      i = i + 2
      continue
    else:
      sum = sum + nums[i]
      i = i + 1
      
  return sum



print(sum13([1, 2, 2, 1])) # 6
print(sum13([1, 1])) # 2
print(sum13([1, 2, 2, 1, 13])) # 6
print(sum13([1, 2, 2, 1, 13, 6, 1])) # 7