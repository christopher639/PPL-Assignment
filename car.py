class Car:
    def __init__(self,name,size,model,capacity):
        self.name = name
        self.size = size
        self.model = model
        self.capacity= capacity
    #information about the car
    def car_information(self):
        car_info = [self.name,self.size,self.model,self.capacity]
        for i in car_info:
            print(f"{i}")
    def car_info(self):
        carInfo ={"Name":"BMW",
                  "SIZE":"S550",
                  "Model" :"Gwagon",
                  "Capacity" :"4"
                  }
        for key , i in carInfo.items():
            print(f"{key} : {i}")
    def car_temperature(self):
        print("Press : 1 to enable the system")
        print("Press : 0 to stop")
        cooling_system = input("The car condtion :")
        if cooling_system  == 1 :
            temp = input("Enter Current Temperature in the car :")
            if temp > 24 :
                print("Cool air activeted ")
            else:
                print("warm air Actived")
        if cooling_system == 0:
            print("Cooling systemstopped")
    def wheels(self):
        wheel_break =input("are breaks applied , enter 1 if yes:")
        if wheel_break == 1:
            print("Vehicle is decelerating :")
        else :
            print("The car is moving with a constant speed:")

#objects
obj1 = Car("Mancedendez","S550","C Class",4)
obj1.car_information()
obj1.car_info()
obj1.car_temperature()
obj1.wheels()