class Demo:
    def __init__(self):
        print("In Constructor")
    def __del__(self):
        print("In Destructor")
def fun():
    print("In Fun")
    obj = Demo()
    print("End Fun")
    #return obj
#retObj = fun()
fun()
print("End Code")
