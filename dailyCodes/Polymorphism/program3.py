class Demo:
    x = 10
    def __eq__(self,obj):
        print("I'm here")
        return obj == obj2
class Memo:
    x = 20
obj1=Demo()
obj2 = Memo()
print(obj1==obj2)   #obj1.__eq__(self,obj2)
