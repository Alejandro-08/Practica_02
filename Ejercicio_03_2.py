# Ejericio_03_2

class Car():
    """Clase tipo coche"""
    def __init__(self, make, model, year):
        """Inicializacion de los atributos"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gasoline_tank= 0
        self.warranty= 0
    def get_descriptive_name(self):
        """ Imprime las caracteristicas en la pantalla"""
        long_name = str(self.year)+' '+self.make + ' '+self.model
        return long_name.title()
    def read_odometer(self):
        """Imprime los kilometros recorrido por el auto"""
        print "This car has " + str(self.odometer_reading) + " miles on it"
    
    def fuel(self):
        print "This car has " + str(self.gasoline_tank) + " liters of gasoline"
    
    def car_warranty(self):
        print "This car has " + str(self.warranty) + " year warranty"
my_new_car = Car('audi','a4',2020) 
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.gasoline_tank = 10
my_new_car.fuel()
my_new_car.warranty = 1
my_new_car.car_warranty()