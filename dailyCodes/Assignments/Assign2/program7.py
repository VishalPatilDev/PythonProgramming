def outer():
    def inner():
        return "Hello,Core2Web!"
    return inner 
    print("In outer function")
if __name__ == "__main__":
    result = outer()()
    print(result)