def decorator(function):
    def wrapper_f():
        print("This is a decorator")
        return function()
    return wrapper_f

@decorator
def hello():
    print("Hello world")

hello()