class Parent:
    z = 30
    def __init__(self):
        print("In Parent Constructor")
        self.x=10
        self.y=20
    def printData(self):
        print(self.x)
        print(self.y)
    @classmethod
    def dispParent(cls):
        print(cls.z)
    def __del__(s):
        print("In Destructor")
obj1 = Parent()
obj1.printData()
obj1.dispParent()
del obj1

