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




# class Human:
#   def __init__(self, name, age, height, race, nationality):
#     self.name = name
#     self.age = age
#     self.height = height
#     self.race = race
#     self.nationality = nationality
  
#   def play_guitar(self):
#     return 'Can play electric guitar'
    


# h1 = Human('john',23, 5.6, 'caucasian', 'US')
# print(h1)

# print(h1.name)
# print(h1.age)
# print(h1.height)
# print(h1.race)
# print(h1.nationality)


# print(h1.play_guitar())



# Homework
# Mobile phones 
# Attrubutes - size, price, ram, brand
# actions - call, text, take_photos, music


# https://www.gsmarena.com/


class MobilePhones:
  def __init__(self, brand="Dummy Brand", model="dummy model", camera="dummy cam", battery="dummy battery", price="dummy price", launch_data="dummy date"):
    
    # Attributes
    self.brand = brand
    self.model = model
    self.camera = camera
    self.battery = battery
    self.price = price
    self.launch_data = launch_data
  
  # Methods
  def call(self):
    return "calling..."
  
  def text(self):
    return "texting..."
  
  def take_photo(self):
    return 'opening camera...'
  

# samsung instance representing MobilePhones class.
# samsung_phone = MobilePhones("Samsung","Galaxy S26", "50 MP, f/1.8, 24mm (wide)", "Li-Ion 4900 mAh","$ 849.00", "2026, February 25")


# # redmi
# redmi_phone = MobilePhones("Redmi", "s2","30MP", "6000 mAH", 500, "2025, Jan")


iphone = MobilePhones()

# Accessing attributes
print(iphone.brand)
print(iphone.model)
print(iphone.camera)
print(iphone.battery)
print(iphone.launch_data)
print(iphone.price)


# Calling methods
print(iphone.call())
print(iphone.text())
print(iphone.take_photo())


# print(samsung_phone.brand)
# print(samsung_phone.model)
# print(samsung_phone.camera)
# print(samsung_phone.battery)
# print(samsung_phone.launch_data)
# print(samsung_phone.price)


# print(samsung_phone.call())
# print(samsung_phone.text())
# print(samsung_phone.take_photo())




# print(redmi_phone.brand)
# print(redmi_phone.model)
# print(redmi_phone.camera)
# print(redmi_phone.battery)
# print(redmi_phone.launch_data)
# print(redmi_phone.price)


# print(redmi_phone.call())
# print(redmi_phone.text())
# print(redmi_phone.take_photo())




# def greet(name="Stranger"):
#   return "Hi " + name


# print(greet())
# print(greet("John"))