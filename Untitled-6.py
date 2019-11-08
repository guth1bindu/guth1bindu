def decorator(func):
    def inner(*args):
        list=[]
        list=args[1:]
        for i in list:
            if i==0:
                return "give proper input"
        return func(*args)
    return inner
@decorator
def div1(a,b):
    return a/b
@decorator
def div2(a,b,c):
    return a/b/c
print(10,5)
print(0,8,5)