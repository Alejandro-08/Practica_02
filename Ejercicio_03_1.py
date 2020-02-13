# Ejercicio_3_1

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
    def read_odometer(self):
        """Imprime los kilometros recorrido por el auto"""
        print("This car has " + str(self.odometer_reading) + " miles on it")
my_new_car = Car('audi','a4',2020)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

"""El cambio en este codigo fue que se modifica el valor del atributo 
predefinido (que esta debajo del constructor), y este no es incluido en el 
constructor, al final de llama al objeto junto con el atributo predefinido
y se le asigna un valor y se manda a llamar al metodo read_odometer"""
