class Vehicle:
    def __init__(self,brand,model,year,speed):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed
    def accelerate(self):
        print("Vehicle:Accelerate")
    def brake(self):
        print("Vehicle:brake")
    def honk(self):
        print("Vehicle:honk")
class Child(Vehicle):
    def accelerate(self):
        print("Child:Accelerate")
    def honk(self):
        print("Child:honk")
obj1 = Vehicle("honda","hero",2022,"80kmph")
obj2 = Child("honda","hero",2022,"80kmph")
