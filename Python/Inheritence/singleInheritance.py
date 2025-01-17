class parent():
    c_name="parent"
    def __init__(self,name):
        self.name=name
        print(name)

class child(parent):
    def __init__(self,name):
        parent.__init__(self,name)

Parent=parent("Rohan")
Child=child("Dubey")
print(Child.c_name)