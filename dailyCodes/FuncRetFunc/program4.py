def outer():
    def inner1():
        print("In inner1");
    def inner2():
        print("In inner2");
    return inner1,inner2
retObj = outer()
for i in retObj :
    i()
