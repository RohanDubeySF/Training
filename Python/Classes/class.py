class A():
    Name='A'
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    def sum(self,a,b):
        sum=a+b
        return sum
    
a=A(5,4)
print(a.Name)
print(a.sum(5,3))