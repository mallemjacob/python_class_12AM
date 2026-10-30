
# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.


def sum67(nums):
  sum = 0
  i = 0
  j = 1
  
  while i < len(nums):  # 6 < 7
    if nums[i] == 6:  # 6 == 6
      while nums[i + j] != 7:  # nums[6]  --> 7 != 7
        j = j + 1 # j = 3
      i = i + j + 1  # i = 7
    else:
      sum = sum + nums[i]
      i = i + 1
  
  return sum
      
  


print(sum67([1, 2, 2])) # 5
print(sum67([1, 2, 2, 6, 99, 99, 7])) # 5
print(sum67([1, 2, 2, 6, 99, 99, 7, 1, 1])) # 7
print(sum67([1, 1, 6, 7, 2])) # 4
