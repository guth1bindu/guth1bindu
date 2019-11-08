def decor(func):
    def inner(year):
        if year<=2018:
            print("sorry your not eligible for job")
        elif year>=2021:
            print("more oppurtinite waiting for you but its its not good time to apply")
        else:
            return func(year)
    return inner
@decor
def wish(year):
    print("your",year,"passedout so you can attend")
wish(2019)
wish(2018)
wish(2016)
wish(2017)