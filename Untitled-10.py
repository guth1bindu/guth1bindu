def outer(exp):
    def upper_i(func):
        def inner():
            return func()+exp
        return inner
    return upper_i
@outer("bindu")
def wish():
    return "good morning"
print(wish())