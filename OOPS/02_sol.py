# class Car:
#    def __init__(self, brand, model):
#        self.brand = brand
#        self.model = model

#     def full_name(self):
#         return f"{self.brand}{self.model}"
        
    
# my_car = Car("toyota","corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_new_car = Car("tata","safari")
# print(my_new_car.model)



class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)