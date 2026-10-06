# Class - We can represent real world objects.

# Human beings 
# --> Attributes = homo sapines, intelligent, 2 hands, 1 head
# --> Actions = can talk, can think, can run


# fruits = ['apple','banana','cherry']

# fruits.index('apple')  # 0




# def greet(name, age):  # name = mouse
#   name = name  # newname = mouse
#   age = age
#   return {name,age}

# newmouse = greet('mouse', 10)
# print(newmouse)

# def hi(name):
#   print('Good morning ' + name)
  
# hi('p1')
# hi('p2')
# hi('p3')



# Dog 
# --> Attributes = name, age
# --> Actions = bark, run, play

# # Blueprint
# class Dog:
  
#   def __init__(self, name, age):
#     # Attributes
#     self.name = name
#     self.age = age
  
  
#   def bark(self, bark_type):
#     print(bark_type)
  
    
  
# # newdog Object or instance of Dog

# # Dog object 1
# dog1 = Dog('snoopy',7)

# print(dog1.name)
# print(dog1.age)

# dog1.bark('Bow Bow!!!')

# print('---------------------------------------')

# # Dog object 2
# dog2 = Dog('zophie', 10)

# print(dog2.name)
# print(dog2.age)

# dog2.bark('Boo Boo!!')

# print('---------------------------------------')

# # Dog object 3
# dog3 = Dog('peppa pig', 5)

# print(dog3.name)
# print(dog3.age)

# dog3.bark('Moew Moew!!')    

# # time: 10 AM
# # what is this?

# # time: 11 AM
# # what is this?




class Human:
  def __init__(self, name, age, height, race, nationality):
    self.name = name
    self.age = age
    self.height = height
    self.race = race
    self.nationality = nationality
  
  def play_guitar(self):
    return 'Can play electric guitar'
    


h1 = Human('john',23, 5.6, 'caucasian', 'US')
print(h1)

print(h1.name)
print(h1.age)
print(h1.height)
print(h1.race)
print(h1.nationality)


print(h1.play_guitar())



# Homework
# Mobile phones 
# Attrubutes - size, price, ram, brand
# actions - call, text, take_photos, music


# https://www.gsmarena.com/