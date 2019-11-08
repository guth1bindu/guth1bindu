class Student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
    def msg(self):
        return self.name+" got grade "+self.grade
s=Student("bindu","A")
s.grade="B"
print(s.name)
print(s.grade)
print(s.msg())