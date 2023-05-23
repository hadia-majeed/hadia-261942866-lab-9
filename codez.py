#Qno1
from math import pi

class Shape:
    def __init__  (self, sides):
        self.sides = sides
    def ComputArea(self):
        pass
class Triangle(Shape):
    def __init__ (self, base, height):
        super().__init__(3)
        self.base = base
        self.height = height
    def ComputArea(self):
        return 0.5 *self.base * self.height

class Circle(Shape):
    def __init__(self, radius):
        super().__init__(0)
        self.radius = radius
    
    def ComputArea(self):
        return pi * self.radius**2
    
triangle = Triangle(2,4)
print("the area of triangle is:", triangle.ComputArea())
circle = Circle(2)
print("the area of circle is:", circle.ComputArea())

#Qno2 
class Employee:
    def __init__ (self,empname,empID,Salary ):
        self.empname = empname
        self.empID = empID
        self.Salary = Salary

    def SalaryStatus(self):
        return (f"Salary:{self.Salary}")
        
class BuildingManager (Employee):
    def __init__ (self,empname,empID):
        super().__init__(empname,empID,1000)
        super().SalaryStatus()

class ProcurementManager (Employee):
    def __init__ (self,empname,empID):
        super().__init__(empname,empID,2000)
class LogisticManager (Employee):
    def __init__ (self,empname,empID):
        super().__init__(empname,empID,3000)

def main():
    employees = [
        BuildingManager("hadia","123"),
        ProcurementManager("majeed","456"),
        LogisticManager ("bhattI","678")
    ]
    for i in employees:
        print("Employee Name:",i.empname)
        print("Employee ID:",i.empID)
        print(i.SalaryStatus())
        print()
main()

