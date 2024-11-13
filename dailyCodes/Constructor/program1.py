#Initializing variables in constructors and methods
class Demo:
    def __init__(self):
        print("In Constructor")
        self.x =10
        self.y = 20
        
    def setData(self):
        self.z = None
        
    def printData(self):
        print(self.x)
        print(self.y)
        print(self.z)
        

obj = Demo()
obj.setData()
obj.printData()

