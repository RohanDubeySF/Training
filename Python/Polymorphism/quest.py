#Create a base class Employee with a method calculate_salary() that returns a base salary of 50,000. Then, create two derived classes, Manager and Developer, that override the calculate_salary() method to add bonuses specific to their roles. The Manager class should add a bonus of 20,000, and the Developer class should add a bonus of 10,000. Finally, create instances of Manager and Developer, and call their calculate_salary() methods to demonstrate method overriding.

class Employee():
    def calc_salary(self):
        base=50000
        return 50000
    
class Manager(Employee):
    def calc_salary(self):
        base=super().calc_salary()
        return base +20000
    
class Developer(Employee):
    def calc_salary(self):
        base=super().calc_salary()
        return base + 10000

M=Manager()
print(M.calc_salary())

d=Developer()
print(d.calc_salary())