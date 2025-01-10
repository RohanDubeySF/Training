class parent():
    def __init__(self):
        pass
    def hello(self,name):
        print("Hi " + name)

class child(parent):
    def __init__(self):
        pass

p=parent()
p.hello("Parent")

c=child()
c.hello("Child")