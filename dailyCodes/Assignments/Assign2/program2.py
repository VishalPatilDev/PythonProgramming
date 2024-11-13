def outer():
    def inner():
        return "Greetings from the inner function!"
    return inner()
if __name__ == "__main__":
    result = outer()
    print(result)
#print nothing