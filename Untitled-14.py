class Gooty:
    def __init__(self,name,proper):
        self.name=name
        self.proper=proper
    def __call__(self):
        print("enter user name",self.name)
        print("enter your proper name",self.proper)
g=Gooty("bindu","anantapur")
g()     