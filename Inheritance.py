class parent():
    def __init__(self,name):
        self.name=name
        print(name+name+name)
    
class child1():
    def __init__(self,name):
        self.name=name
        print(name+name)

class child2(parent,child1):
    def __init__(self,name):
        super().__init__(name)

parent("Rohan")
child1("Dubey")
child2("child")