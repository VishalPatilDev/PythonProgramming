def decorFun(func):
    def wrapper():
        print("Start wrapper")
        func()
        print("End wrapper")
    return wrapper
@decorFun
def normalFunc():
    print("In Normal Func")
#normalFunc = decorFun(normalFunc)
normalFunc()
