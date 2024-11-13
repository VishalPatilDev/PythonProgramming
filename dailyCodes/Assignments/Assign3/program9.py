class Parent:
    @classmethod
    def compName(self):
        print("In Class Method")
    
    @staticmethod
    def comp():#no need to write self in static  method
        print("In Static Method")
    
    def employee(self):
        print("In Instance Method")
class Child(Parent):
    pass

obj  = Child()
obj.classMethod()
obj.staticMethod()

obj.instanceMethod()