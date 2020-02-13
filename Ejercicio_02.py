# Ejercicio 2
# • 

class Car():
    """Clase tipo coche"""
    def __init__(self, make, model, year):
        """Inicializacion de los atributos"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """ Imprime las caracteristicas en la pantalla"""
        long_name = str(self.year)+' '+self.make + ' '+self.model
        return long_name.title()
    def read_odometer(sefl):
        """Imprime los kilometros recorrido por el auto"""
        print("This car has " + str(sefl.odometer_reading) + " miles on it")
        
my_new_car = Car('audi','a4',2020) 
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

"""Al correrlo observe que aparece lo mismo que lo anterior, solo que esta vez
se le agrego un metodo más y a este metodo un mensaje, y que determinara el 
kilometraje del carro que si observamos bien, en la parte de los atributos
se le ha agregado un atributo igualado a 0, sin introducir el parametro en el 
constructor"""

# • 

class Car():
    """Clase tipo coche"""
    def __init__(self, make, model, year):
        """Inicializacion de los atributos"""
        self.make = make
        self.model = model
        self.year = year
        
    def get_descriptive_name(self):
        """ Imprime las caracteristicas en la pantalla"""
        long_name = str(self.year)+' '+self.make + ' '+self.model
        return long_name.title()
    def read_odometer(self):
        """Imprime los kilometros recorrido por el auto"""
        print("This car has " + str(self.odometer_reading) + " miles on it")
        
my_new_car = Car('audi','a4',2020) 
print(my_new_car.get_descriptive_name())
#my_new_car.read_odometer(self.odometer_reading=0)
#my_new_car.read_odometer(self)
"""De ninguna manera va a poder correr el programa, porque le estoy colocando 
un atributo no definido en el contructor a el objeto creado, y en este no van 
los parametros, mucho menos un atributo, el self es propio de una función, mas
no al llamar con el objeto a un atributo."""
""" También estaba mal escrito el self en el metodo read_odometer y  estaba 
como sefl y lo correji, pero aun asi no corre el programa"""
# • 

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
        
my_new_car = Car('audi','a4',2020) 
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()