from pathlib import Path


# path = Path('./pi.txt')

# # Reading a file.
# contents = path.read_text()

# if contents:
#   print('not empty')
# else:
#   print('empty')

# Writing to a file.

print('Enter a cat name:')
cat_name = input()
if cat_name:
  path = Path('cat_names.txt')
  path.write_text(cat_name)
  
  contents = path.read_text()
  
  if contents:
      print('Successfully written to the file!')
      print('The cat name is ' + contents)
  else:
    print('The file is empty!')
else:
  print('Enter something.') 