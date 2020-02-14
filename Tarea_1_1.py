# Tarea_1_1

class Restaurant():
    def __init__(self, name, type, open):
        self.restaurant_name=name
        self.cuisine_type=type
        self.number_served = 0
        
    def describe_restaurant(self):
        print("\nThe name of the restaurant is " + self.restaurant_name + '.')
        print("The restaurant is of the " + self.cuisine_type + " type" + '.')
        
    def open_restaurant(self):
        print("The restaurant is " + str('open') + '.')
        
    def served(self):
        print(str(self.number_served) + " customer were served")
        
    def update_number_served(self, customers):
        
        if customers >= self.number_served:
            self.number_served= customers
        else:
            print("there are no negative customers")
Restaurante=Restaurant('the flavor cellar','cuisine traditional','open')
Restaurante.describe_restaurant()
Restaurante.open_restaurant()
Restaurante.served()
Restaurante.update_number_served(15)
Restaurante.served()
