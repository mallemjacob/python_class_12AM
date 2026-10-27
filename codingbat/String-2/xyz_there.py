# Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.

def xyz_there(str):


print(xyz_there('abcxyz')) # True
print(xyz_there('abc.xyz')) # False
print(xyz_there('xyz.abc')) # True