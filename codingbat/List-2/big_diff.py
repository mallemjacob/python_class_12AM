
# Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.


# def big_diff(nums):
#   return max(nums) - min(nums)

def big_diff(nums):
  max_num = nums[0] # max_num = 61
  min_num = nums[0]
  
  for num in nums: # 10,13,5,61 --> num = 61
    if num > max_num:  # 61 > 13
      max_num = num  # max_num = 61
    elif num < min_num:
      min_num = num      
  
  return max_num - min_num
  

print(big_diff([10, 13, 5, 61])) # 56
print(big_diff([10, 3, 5, 6])) # 7
print(big_diff([7, 2, 10, 9])) # 8
print(big_diff([2, 10, 7, 2])) # 8

# current_latgest = 61
# 61 > current_latgest