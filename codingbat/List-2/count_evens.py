# Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.


def count_evens(nums):
  even_count = 0
  
  for num in nums:
    if num % 2 == 0:
      even_count = even_count + 1
  
  return even_count

print(count_evens([2, 1, 2, 3, 4])) # 3
print(count_evens([2, 2, 0])) # 3
print(count_evens([1, 3, 5])) # 0
