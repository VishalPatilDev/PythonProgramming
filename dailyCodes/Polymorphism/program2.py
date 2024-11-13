class Demo:
    def fun(self):
        print("In Demo : fun")
class Memo:
    def gun(self):
        print("In Memo : gun")
def callFun(obj):
    if id(obj)==id(obj1):
        obj.fun()
    else:
        obj.gun()
    '''
    if obj is Demo:
        obj.fun()
    elif obj is Memo:
        obj.gun()
    '''
obj1 = Demo()
obj2 = Memo()
callFun(obj2)
