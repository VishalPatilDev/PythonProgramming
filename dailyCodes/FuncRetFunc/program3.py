def outer():
    def inner1():
        print("In inner1 func")
    def inner2():
        print("In inner2 func")
    return inner1,inner2
    print("In outer func")
retObj = outer()
print(retObj)

'''
inn1,inn2 = outer()
inn1()
inn2()

'''
'''
retObj = outer()
for i in retObj:
    i()

'''

