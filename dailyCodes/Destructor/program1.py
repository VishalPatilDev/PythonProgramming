class Parent:
    z = 30
    def __init__(self):
        print("In Parent Constructor")
        self.x = 10
        self.y = 20
    def printData(self):
        print(self.x)
        print(self.y)
    def __del__(self):
        print("In Destructor")
obj = Parent()
obj.printData()
#obj.__del__()
