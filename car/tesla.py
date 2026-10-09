from electric_car import ElectricCar
from car import SuperCar

class Tesla(ElectricCar):
  def __init__(self, make, model, year, battery_size):
   super().__init__(make, model, year, battery_size)
   
   
t1 = Tesla('t1_maker', 't1_model', 2030, 1000)

t1.battery.describe_battery()


      #  car
      #   |
      #   |
      #   ElectricCar <-- Battery
      #   |
      #   |
      # Tesla
      

s1 = SuperCar('super maker', 'super model')

print(s1.make)
print(s1.model)