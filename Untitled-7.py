def function1():
    print("hi this is function1")
def function2(func):
    print("hi this is function2")
    func()
function2(function1)
