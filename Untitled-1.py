def decor(func):
    def inner(phone):
        if phone=="samsung":
            print("sorry samsung phones are out of service")
        else:
            func(phone)
    return inner
@decor
def new(phone):
    print("congratulation",phone,"mobile is available")
new("samsung")
new("micromax")
new("realme")
        