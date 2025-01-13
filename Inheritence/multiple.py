class A:
    name="Parent"
    def __init__(self,name,surname):
        print("This is a Parent Class A")
        self.name = name
        self.surname = surname

class B():
    def __init__(self,Branch):
        print("This is a Parent Class B")
        self.Branch=Branch
        

class C(A,B):
    def __init__(self,name,surname,Branch,city):
        print("This is a child Class of A & B")
        A.__init__(self,name,surname)
        B.__init__(self,Branch)
        self.city=city
        
    def prit(self):
        print(f"{self.name} {self.surname} {self.Branch} {self.city}")
#A()
#B()
obj=C("Rohan","Dubey","AI","Ahm")
obj
obj.prit()