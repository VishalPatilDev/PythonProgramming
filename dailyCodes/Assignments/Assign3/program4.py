class Parent:
    def __init__(self,a,b):
        self.a =a
        self.b = b
    def m1(self,a,b):
        return self.a+self.b
class Child(Parent):
    pass
obj = Child(10,20)
ret = obj.m1(10,20)

print(ret)    