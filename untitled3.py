def decor(func):
    def inner(eligible):
        if eligible<=2018:
            print("your not eligible for job")
        else:
            func(eligible)
    return inner
@decor
def wish(eligible):
    print("your eligible for interview")
wish(2019)
wish(2017)