def decorFun(func):
    def wrapper(*args):
        print("Start wrapper")
        val = func(*args)
        print("End wrapper")
        return val
    return wrapper
@decorFun
def normalFunc(x,y):
    print("In NormalFunction")
    return x+y
#normalFunc =  decorFun(normalFunc)
print(normalFunc(10,20))
