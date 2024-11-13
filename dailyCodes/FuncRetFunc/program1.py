def outer(x,y):
    def inner():
        print("In Inner Function")
    print("In Outer Function")
    return inner
retObj = outer(10,20)
retObj()
