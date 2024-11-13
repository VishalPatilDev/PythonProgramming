def decorFun(func):
    def wrapper():
        print("Start wrapper2")
        func()
        print("End wrapper2")
    return wrapper
def decorRun(func):
    def wrapper():
        print("Start wrapper1")
        func()
        print("End wrapper1")
    return wrapper
@decorFun
@decorRun
def normalFun():
    print("In Norm Fun")
#normalFun = decorFun(decorRun(normalFun))
normalFun()
