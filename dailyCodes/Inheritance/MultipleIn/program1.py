class Parent1:
    def __init__(self):
        print("In Parent Constructor")
    def dispData(self):
        print("In dispData")
class Parent2:
    def __init__(self):
        print("In Parent2 Constructor")
    def printData(self):
        print("In printData")
class Child(Parent2,Parent1):
    pass
obj = Child()
obj.dispData()
obj.printData()
print(Child.mro())
