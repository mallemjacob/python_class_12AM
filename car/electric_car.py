# from [filename] import [Class]
from car import Car, SuperCar
from battery import Battery


# import entire module
# import car
# supercar_1 = car.SuperCar('benz', 'supersonic')


# import all classes from a module
# from car import *



class ElectricCar(Car):
  def __init__(self, make, model, year, battery_size):
    super().__init__(make, model, year)
    # Child attibutes
    self.battery = Battery(battery_size)
  
  # Override the parent's method.
  def get_details(self):
    return 'This is an electric car.'
  
# my_leaf is an instance of a ElectricCar class
my_leaf = ElectricCar('Nissan','leaf',2026, 100)  

print(my_leaf.get_details())
my_leaf.battery.describe_battery()
