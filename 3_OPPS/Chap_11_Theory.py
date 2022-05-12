
                            # Chapter 11:- Inheritance
                            
''' 
    - Inheritance is a way of crating a new class from an existing class.
    - Example:
                class Employee:
                    # Code          -----> This is 'Base' or 'Parent' Class
                
                class Programmer(Employee):
                    # Code          ------> This is 'Derived' or 'Child' Class

    - We can use the methods and attributes of Employee('Parent') Class in Programmer('Child') Class.
    - Also, we can override or add new attributes and methods in Programmer(Child) class.

    - Types of Inheritace:- 
    1) Single Inheritance - It occurs when child class inherits only a sigle parent class.
    2) Multiple Inheritance - It occurs when a child class inherits from more than one parent class.
    3) Multilevel Inheritance - When child class become a parent for another child class.
'''



"________________________X______________________ Single Inheritance  ________________________X_________________________"


class Employee:
    company = "Google"

    def ShowDetails(self):
        print("This is an employee!")

class Programmer(Employee):
    language = "Python" 
    # company = "YouTube"

    def getlanguage(self): 
        print(f"The language is {self.language}")

    def ShowDetails(self):
        print("This is a Programmer!")

e = Employee()
e.ShowDetails()
print(e.company)
p = Programmer()
p.ShowDetails()
print(p.company)


"________________________X______________________ Multiple Inheritance  ________________________X_________________________"

class Employee:
    company = "Visa"
    EmpID = 85

class Freelancer:
    company = "Fiverr"
    level = 0

class Porgrammer(Freelancer, Employee): # "" Here Freelancer comes 1st so it will get first priority."" 
    name = "Bhavik"

p = Porgrammer()
print(p.company)


"________________________X______________________ Multilevel Inheritance ________________________X_________________________"

class Grandpa:
    Country = "'India'"

    def takeBreath(self):
        print("I'm breathing")


class Daddy(Grandpa):
    Company = "Reliance"

    def getSalary(self):
        print(f"Salary is {self.salary}")
    
    def takeBreath(self):
        print("I am employee so I'm Luckily breathing")

class Son(Daddy):
    company = "Fiverr"

    def getSalary(self):
        print("No salary to programmers")
    
    def takeBreath(self):
        print("I'm a Programmer so I'm breathing ++..")

g = Grandpa()
d = Daddy()
s = Son()
g.takeBreath()
d.takeBreath()
s.takeBreath()
print(s.Country)


#"________________________X______________________ Super Method ________________________X_________________________"

" Super Method : It is use to access the methods of a super class in the derived class.      "

class Grandpa:
    def __init__(self):
        print("Initializing Grandpa....\n")

    def takeBreath(self):
        print("I'm breathing")

class Daddy(Grandpa):    
    def __init__(self):
        super().__init__()
        print("Initializing Daddy.....\n")    

    def takeBreath(self):
        super().takeBreath()
        print("I am employee so I'm Luckily breathing")

class Son(Daddy):
    def __init__(self):
        super().__init__()
        print("Initializing Son.....\n")

    def takeBreath(self):
        super().takeBreath()
        print("I'm a Programmer so I'm breathing ++..")

g = Grandpa()
d = Daddy()
s = Son()

