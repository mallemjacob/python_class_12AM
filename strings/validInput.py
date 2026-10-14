while True:
  print('Enter your age: ')
  age = input() #21
  if age.isdecimal():
    break
  print('Please enter a number for your age')
  
  
while True:
  print('Select a new password (letter and numbers only):')
  password = input()
  if password.isalnum():
    break
  print('Password can only have letters and numbers')