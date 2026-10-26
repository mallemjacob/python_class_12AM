# Reading from a file

# from pathlib import Path

# path = Path('pi_digits.txt')
# contents = path.read_text()
# contents = contents.rstrip()

# print(contents)
# print(len(contents))


# Relative and Absolute Paths

# C:\Usrs\Al\Documents\porjects\hello.pdf


# /home/valkyrie/Desktop/python_class_12AM

#             /
#               home
#                 valkyrie
#                   Desktop

# Accessing File lines
# from pathlib import Path

# path = Path('./pi_digits.txt')
# contents = path.read_text()

# lines = contents.splitlines()

# pi_string = ''

# for line in lines:
#   pi_string = pi_string + line
  
# print(pi_string)
# print(len(pi_string))


# Large Files

# from pathlib import Path

# path = Path('./pi_million_digits.txt')
# contents = path.read_text()

# lines = contents.splitlines()

# pi_string = ''

# for line in lines:
#   pi_string = pi_string + line.lstrip()
  
# print(f"{pi_string[:52]}...")
# print(len(pi_string))


# Writing to a File

# from pathlib import Path

# path = Path('./python_datas', 'new_programming.txt')

# contents = 'I am learning python programming language!\n'
# contents = contents + "I want to learn other libraries like fastAPI.\n"
# contents += "I work with huge data!"


# try:
#   path.write_text(contents)
# except FileNotFoundError:
#   print("Invalid path!")

# contents = path.read_text()

# print('The contents are stored successfully!')
# print(contents)


# Exception handling