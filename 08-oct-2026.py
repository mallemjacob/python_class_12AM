# Inheritance

# parent --> genes inherit --> children 


# Parent class
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

my_car = Car('Tesla','T1',2025)

print(my_car.make)
print(my_car.model)
print(my_car.year)

print(my_car.get_details())


##############################################################
  
# Instances as attribute

class Battery:
  def __init__(self, battery_size=40):
    self.battery_size = battery_size
    
  
  def describe_battery(self):
    print("This car has " + str(self.battery_size) + '--KWh battery.')


# b1 = Battery(120)
# b1.describe_battery()


##############################################################


# Child class
class ElectricCar(Car):
  def __init__(self, make, model, year, battery_size):
    super().__init__(make, model, year)
    # Chlid attibutes
    self.battery = Battery(battery_size)
  
  # Override the parent's method.
  def get_details(self):
    return 'This is an electri car.'
  
# my_leaf is an instance of a ElectricCar class
my_leaf = ElectricCar('Nissan','leaf',2026, 100)  

print(my_leaf.make)
print(my_leaf.model)
print(my_leaf.year)

print(my_leaf.get_details())
my_leaf.battery.describe_battery()




            #        Car
            #         |
            #         |
      #      -----------------
      #      |                |
  # ElectriCar (Battery)  SportCar
  



# varibale --> arrtibute
# name = "mouse"


# function --> method
# def greet():
#   return 'hi'  + name