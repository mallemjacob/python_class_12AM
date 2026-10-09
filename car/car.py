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


# SuperCar class
class SuperCar:
  def __init__(self, make, model):
    self.make = make
    self.model = model
    
