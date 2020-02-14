# Ejercicio_7_2
class Car():
	
    """Un intento de representar un auto""" 
	
    def __init__(self, make, model, year):
		self.make = make 
		self.model = model 
		self.year = year 
		self.odometer_reading = 0
	
    def get_descriptive_name(self):
		
        long_name = str(self.year) + ',' + self.make + ',' + self.model 
		
        return long_name.title()
	
    def read_odometer(self): 
		print("This car has " + str(self.odometer_reading) + " miles on it.")
	
    def update_odometer(self, mileage):
		
        if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
		self.odometer_reading += miles

class ElectricCar(Car):
	def __init__(self, make, model, year):
		Car.__init__(self,make,model,year)

my_tesla = ElectricCar('tesla','model s',2020) 
print(my_tesla.get_descriptive_name())

class HybridCar(Car):
	def __init__(self,make,model,year):
        
		Car.__init__(self,make,model,year)
my_Hybridcar = HybridCar('Toyota','Prius',2020) 
print(my_Hybridcar.get_descriptive_name())

class FuelCar(Car):
    def __init__(self,make,model,year):
		Car.__init__(self,make,model,year)
		self.tank_gasoline = 25
   
    def tank(self):
		print("This car has a " + str(self.tank_gasoline) + " liters of gasoline")

my_tesla = ElectricCar('tesla','model s',2020) 
print (my_tesla.get_descriptive_name())
my_tesla.get_descriptive_name()

my_FuelCar = FuelCar('Toyota','Pirus',2020) 
print (my_FuelCar.get_descriptive_name())
my_FuelCar.tank()