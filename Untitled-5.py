def decor(func):
    def inner(m,n):
        if n==0:
           print("we cannot division with '0'")
        else:
            func(m,n)
    return inner
@decor
def wish(m,n):
    return m/n
print(wish(10,2))
print(wish(123,12))
print(wish(324,5))
print(wish(12,0))