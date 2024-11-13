class Parent:
    def __init__(self):
        print("In Parent Constructor")
        self.x = 10
        self.y = 20
    def printData(self):
        print(self.x)
        print(self.y)
class Child(Parent):
    pass
obj = Child()
obj.printData()
print(obj.printData)
del obj

