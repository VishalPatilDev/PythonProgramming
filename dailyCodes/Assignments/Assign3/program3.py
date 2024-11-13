class Parent:
    @classmethod
    def classMethod(self):
        print("In Class Method")
    
    @staticmethod
    def staticMethod():#no need to write self in static  method
        print("In Static Method")
    
    def instanceMethod(self):
        print("In Instance Method")
class Child(Parent):
    pass

obj  = Child()
obj.classMethod()
obj.staticMethod()

obj.instanceMethod()