class Decorater:
    def __init__(self,func):
        self.func=func
    def __call__(self):
        str=self.func()
        return str.split()
class Decorater_1:
    def __init__(self,cap):
        self.cap=cap()
    def __call__(self):
        str1=self.cap
        return str1.upper()       
@Decorater
@Decorater_1
def greet():
    a=input("enter a name")
    b=input("enter your proper")
    return a,b
print(greet())