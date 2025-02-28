class Car:
    total_car = 0
    def __init__(self, brand, model):
       self.__brand = brand
       self.__model = model
       Car.total_car += 1
       
    def get_brand(self):
        return self.__brand + " !"
        
       
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(Self):
        return "gasoline"
    
    
    @staticmethod
    def general_desc():
        return "cars are means of transport"
    
    
    @property
    def model(self):
        return self.__model
    
    
class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
    def fuel_type(Self):
        return "Electric charge"
        
        
        
my_tesla = ElectricCar("Tesla","Model S","85kwh")
# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))
# print(my_tesla.full_name())
# print(my_tesla.__brand)

# print(my_tesla.fuel_type())

# safari = Car("tata","safaris")
# # safari.model = "city"
# print(safari.model)
# print(safari.fuel_type())
# print(safari.total_car)

# print(safari.general_desc())
# print(Car.general_desc())



class Battery:
    def battery_info(self):
        return "Battery is a component of electric cars"

class Engine:
    def engine_info(self):
        return "Engine is a component of cars"


class ElectricCarTwo(Battery, Engine, Car):
    pass




my_new_tesla = ElectricCarTwo("tesla","model s")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())
    
