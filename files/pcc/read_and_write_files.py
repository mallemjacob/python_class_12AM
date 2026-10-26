# Files and Strings

# from pathlib import Path

# # Define the path
# path = Path('./python_data', 'hello.txt')

# # write_text() --> Write to files

# data = '''
# Python is widely taught as an introductory programming language.[41]

# History
# Main article: History of Python

# The name Python derives from the British comedy series Monty Python's Flying Circus.[47] (See § Naming.)

# Python uses dynamic typing and a combination of reference counting and a cycle-detecting garbage collector for memory management.[64] It uses dynamic name resolution (late binding), which binds method and variable names during program execution.
# '''

# path.write_text(data)

# # read_text() --> Read from files
# contents = path.read_text(encoding='utf-8')

# print('--------------------------')
# print(contents)






# Analyze text
from pathlib import Path

def count_words(path):
  try:
    contents = path.read_text(encoding='utf-8')
  except FileNotFoundError:
    print(f"Sorry, the file {path} does not exits.")
  else:
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")
    
    
alice_path = Path('alice.txt')
hello_path = Path('./python_data/hello.txt')
count_words(hello_path)

# JSON
# frint_end (react) ---> backend (python, fastapi)


