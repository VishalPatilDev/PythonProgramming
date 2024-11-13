def outer(a,b):
    def inner(a,b):
        print("In inner func")
        return a+b
    print("In outer func")
    print(a*b)
    return inner
retObj1 = outer(10,20)
retObj2 = retObj1(30,40)
print(retObj2)
#print(retObj1)  --- It will return address of inner function


