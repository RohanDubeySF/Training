class parent():
    def __init__(self,name):
        self.name=name
        print(name)

class child(parent):
    def __init__(self,name):
        super().__init__(name)

parent("Rohan")
child("Dubey")
