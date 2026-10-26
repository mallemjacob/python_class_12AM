# dump JSON data

# from pathlib import Path
# import json

# numbers = [2,3,5,7,9,11]

# path = Path('numbers.json')

# contents = json.dumps(numbers)

# print(contents)

# path.write_text(contents)



# Load JSON data

# from pathlib import Path
# import json

# path = Path('numbers.json')

# contents = path.read_text()

# numbers = json.loads(contents)

# print(numbers)


# User Generated data

from pathlib import Path
import json

username = input("What is your name? ")

path = Path('username.json')
contents = json.dumps(username)
path.write_text(contents)


print(f"Hello {username}")





