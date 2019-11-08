class Divison:
    def __init__(self,func):
        self.func=func
    def __call__(self,*args,**kwargs):
        list=[]
        list=args[1:]
        for i in list:
            if i==0:
                return "we can't divide with zero"
        else:
            return self.func(*args,**kwargs)
@Divison
def div(a,b):
    return a/b
@Divison
def div1(a,b,c):
    return a/b/c
@Divison
def div2(a,b,c,d):
    return a/b/c/d
print(div(2,0))
print(div1(0,3,4))
print(div2(16,8,4,2))