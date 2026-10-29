# Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.

def xyz_there(str):
  for i in range(len(str)): # 0,1,2,3 --> i = 1
    if str[i:i + 3] == 'xyz': # str[1:4] --> xyz
      if i == 0 or str[i - 1] != '.': # '.' != '.'
        return True
  
  return False
      


print(xyz_there('abcxyz')) # True
print(xyz_there('abc.xyz')) # False
print(xyz_there('xyz.abc')) # True
print(xyz_there('.xyz')) # False


# 1. xyz
# 2. must ont have . infront of xyz