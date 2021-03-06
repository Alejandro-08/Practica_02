# Ejercicio_8_2

class Car():
	"""Un intento de representar un auto""" 
	def __init__(self, make, model, year):
		self.make = make 
		self.model = model 
		self.year = year 
		self.odometer_reading = 0
	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model 
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
	def charge(self): 
		print("The car is charging ....")

class ElectricCar(Car):
	"""Un intento de representar un auto electrico""" 
	def __init__(self,make,model,year):
		""" Inicializa los atributos de la clase padre """
		Car.__init__(self,make,model,year)
		self.battery_size = 70
	def describe_battery(self):
		""" Imprime la el tamanio de la bateria """
		print("This car has a " + str(self.battery_size) + "-kWh battery.")
	def charge(self): 
		print("the car is not loaded, therefore it is immobilized")

class HybridCar(Car):
	"""Un intento de representar un auto electrico""" 
	def __init__(self,make,model,year):
		""" Inicializa los atributos de la clase padre """ 
		Car.__init__(self,make,model,year)
		self.battery_size = 70
		self.tank_gas= 40
	def describe_meditions(self):
		""" Imprime la el tamanio de la bateria """
		print("This car has a " + str(self.battery_size) + "-kWh battery."+'and'+str(self.tank_gas)+'liters of gasoline')
	def charge(self): 
		print("the car is not loaded, therefore it is immobilized")

class FuelCar(Car):
	def __init__(self,make,model,year):
		Car.__init__(self,make,model,year)
		self.tank_gasoline = 25
	def tank(self):
		print("This car has a " + str(self.tank_gasoline) + " liters of gasoline")
	def charge(self): 
		print("The car is not loaded, therefore it is immobilized")


my_tesla = ElectricCar('tesla','model s',2020) 
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.charge()

my_hybrid_car = HybridCar('Toyota','Pirus',2020) 
print(my_hybrid_car.get_descriptive_name())
my_hybrid_car.describe_meditions()
my_hybrid_car.charge()

my_FuelCar = FuelCar('Toyota','Camry',2020) 
print(my_FuelCar.get_descriptive_name())
my_FuelCar.tank()
my_FuelCar.charge()