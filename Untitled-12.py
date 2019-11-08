import functools
def decor(func):
    @functools.wraps(func)
    def inner(str):
        s=str.upper()
        return s
    return inner
@decor
def wish(str):
    return "good morning" 
print(wish.__name__)