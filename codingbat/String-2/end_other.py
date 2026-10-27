
# Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.


def end_other(a, b):
  a = a.lower()
  b = b.lower()
  
  if len(a) > len(b):
    return a[-len(b):] == b
  elif len(a) < len(b):
    return b[-len(a):] == a
  elif a == b:
    return True
  else:
    return False
    
    

print(end_other('Hiabc', 'abc')) # True
print(end_other('AbC', 'HiaBc')) # True
print(end_other('abc', 'abXabc')) # True  