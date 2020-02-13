# Ejercicio_04_2
class Car():
    """Clase tipo coche"""
    def __init__(self, make, model, year):
        """Inicializacion de los atributos"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gasoline_tank= 10
        self.warranty= 1 
    def get_descriptive_name(self):
        """ Imprime las caracteristicas en la pantalla"""
        long_name = str(self.year)+' '+self.make + ' '+self.model
        return long_name.title()
    def read_odometer(sefl):
        """Imprime los kilometros recorrido por el auto"""
        print("This car has " + str(sefl.odometer_reading) + " miles on it")
    def update_odometer(self, mileage):
        """Modifica el valor del metodo desde la funcion"""
        self.odometer_reading = mileage   
    
    def fuel(self):
        print "This car has " + str(self.gasoline_tank) + " liters of gasoline"
    
    def update_fuel(self,gasoline):
        self.gasoline_tank = gasoline
    
    def car_warranty(self):
        print "This car has " + str(self.warranty) + " year warranty"
        
    def update_warranty(self,insurance):
        self.warranty = insurance
        
my_new_car = Car('audi','a4',2020) 
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()
my_new_car.update_fuel(10)
my_new_car.fuel()
my_new_car.update_warranty(1)
my_new_car.car_warranty()