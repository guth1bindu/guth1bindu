def cheak_name(method):
    def inner(str):
        if str.name=="bindu":
            print("hey my name is also bindu")
        else:
            method(str)
    return inner
class Prac: 
    def __init__(self,name):
        self.name=name      
    @cheak_name
    def hai(self):
        print("enter your name",self.name)
P=Prac("bindu")
P.hai()
R=Prac("naveen")
R.hai()
S=Prac("jagadeesh")
S.hai()