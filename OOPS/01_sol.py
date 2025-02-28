# class Car:
#    def __init__(self, brand, model):
#        self.brand = "BMW"
#        self.model = "M3"
    
# my_car = Car("toyota","corolla")
# print(my_car.brand)
# print(my_car.model)

# my_new_car = Car("tata","safari")
# print(my_new_car.model)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
# p1=Person("Ayush",22)
# print(p1.name)
# print(p1.age)


# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
        
#     def __str__(self):
#         return f"{self.name}({self.age})"
    
# p1=Person("Ayush",22)
# # print(p1.name)
# # print(p1.age)    

# print(p1)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def myFunc(self):
        print("hello my name is "+ self.name)
        
        
p1 = Person("John", 36)
p1.myFunc()
        


        
        