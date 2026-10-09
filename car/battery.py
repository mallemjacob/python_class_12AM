class Battery:
  def __init__(self, battery_size=40):
    self.battery_size = battery_size
    
  
  def describe_battery(self):
    print("This car has " + str(self.battery_size) + '--KWh battery.')


# b1 = Battery(120)
# b1.describe_battery()
