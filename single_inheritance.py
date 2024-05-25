class Vehicle :
    def info(self):
        print('This is Vhicle')

class Car(Vehicle):
    def car_info(self,name):
        print("Car name is :",name)

class Truck(Vehicle):
    def truck_info(self,name):
        print("Truck name is :", name)

#creatin g onjects
obj1 = Car()
obj1.info()
obj1.car_info("BMW")

obj2 = Truck()
obj1.info()
obj2.truck_info("MAN")


        