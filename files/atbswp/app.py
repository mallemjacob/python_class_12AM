from pathlib import Path
import json

# myFiles = ['accounts.txt', 'details.csv', 'invite.docx']

# for filename in myFiles:
#   print(Path(r'/home/valkyrie/python', filename))
  
numbers = [2, 3, 5, 7, 11, 13]

path = Path('numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)