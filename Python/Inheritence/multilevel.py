class A:
    name="Parent"
    def __init__(self,name,surname):
        print("This is a Parent Class A")
        self.name = name
        self.surname = surname

class B(A):
    def __init__(self,name,surname,Branch):
        print("This is a Child Class of A : B")
        self.Branch=Branch
        A.__init__(self,name,surname)
        

class C(B):
    def __init__(self,name,surname,Branch,city):
        print("This is a child Class of B : C")
        B.__init__(self,name,surname,Branch)
        self.city=city
        
    def prit(self):
        print(f"{self.name} {self.surname} {self.Branch} {self.city}")
#A()
#B()
obj=C("Rohan","Dubey","AI","Ahm")
obj
obj.prit()