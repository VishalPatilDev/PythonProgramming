class Parent:
    def __init__(self):
        print("In Parent Constructor")
    def parentFun(self):
        print("In Parent Function")

class Child(Parent):
    def __init__(self):
        print(id(Parent.__init__(self)))
        print(id(super().__init__()))
        print("In Child Constructor")
    def childFun(self):
        print("In Child Function")
obj = Child()
obj.parentFun()
obj.childFun()


