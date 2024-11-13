def fun():
    yield 10
    yield 20
def run():
    return 30
gen = fun()
norm = run()
print(type(fun))
print(type(run))
print(type(gen))
print(type(norm))
