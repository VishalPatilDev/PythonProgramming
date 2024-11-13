class Parent:
    def __init__(self):
        print("In Parent Constructor")
    def parentFun(self):
        print("In Parent Function")

class Child(Parent):
    def __init__(self):
        print("In Child Constructor")

obj = Child()
obj.parentFun()
