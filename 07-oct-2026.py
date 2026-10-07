

class Car:
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
    
    # Setting default values for attributes
    self.odometer_reading = 0

  # modifying an attribute's value through a method.
  def update_odometer(self, milage):
    self.odometer_reading = milage
    
  # getting attribute's value through a method.
  def get_odometer(self):
    return self.odometer_reading
  
  # get car details
  def get_details(self):
    return "This car is made by " + self.make + " and the model is " + self.model + ' and it was released in the year ' + str(self.year)
    

benz = Car('Benz','40A', 2025)

tesla = Car('Telsa','CC4', 2026)
ferrari = Car('Ferrari','aston', 2024)


print(benz.get_odometer())

benz.update_odometer(100)

print(benz.get_odometer())

print(benz.get_details())
print(tesla.get_details())
print(ferrari.get_details())






# # Updating the arrtibute values
# ferrari.odometer_reading = 20
# print(ferrari.odometer_reading)


# if ferrari.odometer_reading == 0: # 20 == 0
#   print("This is a brand new car.")
# else:
#   print("This is a used car.")



# for place in ferrari.only_sold_in_these_places:
#   print("This car is only available in this place: " + place)
  
  
# print(ferrari.engine["model"])
# print(ferrari.engine["price"])




# name = "mouse"


# def get_name():
#   return name

# print(get_name())



# building plan = 3 rooms, 1 kitchen, 1 balcony


# person 1 = house 1
# person 2 = house 2
# person 3 = house 3