def gun():
    print("In Gun")
def run(y):
    print("In run")
    return y
def fun(x):
    print("In fun")
    x()
fun(run(gun))
