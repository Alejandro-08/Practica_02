"""          Practica 02 - Introducción
           Pedro Fernando Flores Palmeros
                Programación avanzada
                    Febrero 2020 
           Fernández Hernández Alejandro   
                      2RV1 
Ingeneria en Sistemas Energeticos y Redes Inteligentes   """

#1.1  Introducción
#  Ejercicio 1

class Car():
    """Clase tipo coche"""
    def _init_(self, make, model, year):
        """Inicializacion de los atributos"""
        self.make = make
        self.model = model
        self.year = year
    def get_descriptive_name(self):
        """ Imprime las caracteristicas en la pantalla"""
        long_name = str(self.year)+' '+self.make + ' '+self.model
        return long_name.title()

my_new_car = Car('audi','a4',2020)
print(my_new_car.get_descriptive_name())

"""Lo que observe que al determinar un objeto de tipo Car, imprime sus
atributos propios de la clase, en orden como es determinado con el metodo, que 
seria primero el año, la marca y el modelo """

