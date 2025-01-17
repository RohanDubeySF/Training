class parent():
    def __init__(self):
        pass
    def hi(self,name):
        print("Hi " + name)

class child(parent):
    def __init__(self):
        pass
    def hi(self,name):
        print("Hello "+ name)

p=parent()
p.hi("Parent")

c=child()
c.hi("Child")