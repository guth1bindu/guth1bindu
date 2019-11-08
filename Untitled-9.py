def upper_s(func):
    def inner():
        s1=func()
        return s1.upper()
    return inner
def split_s(func):
    def wrapper():
        s2=func()
        return s2.split()
    return wrapper
@split_s
@upper_s
def string():
    n=input("enter a string")
    return n
print(string())