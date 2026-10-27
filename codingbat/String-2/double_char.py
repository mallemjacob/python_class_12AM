# Given a string, return a string where for every char in the original, there are two chars.


def double_char(str):
  final_str = ''
  
  for char in str:
    final_str += char * 2
  
  return final_str
  


print(double_char('The')) # 'TThhee'
print(double_char('AAbb')) # 'AAAAbbbb'
print(double_char('Hi-There')) # 'HHii--TThheerree'