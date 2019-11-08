def outer_fun():
    print("outer function excution")
    def inner_fun():
        print("inner function excution")
    print("haiii")
    return inner_fun
f1=outer_fun()
