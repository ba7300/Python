
#                                   Object Oriented Programming
'''                     
Solving a problem by creating object is one of the most popular approach in programing. This is called OOP's 
This concept focuses on using reusable code.
Implement by DRY(Don't Repeat yourself) Principle. 
It is a programming approach that primarily focuses on using objects and classes. 
The objects can be any real-world entities.
'''


#   Class :
'''
The class is a blueprint for creating object. 
It contains information to create a valid object.
'''
#   Object :
'''
An object is an instantiation of a class. When a class is defined, a template(info.) is defined. 
Memory is allocated only after the object instantiation.
'''

#   ABSTRACTION :
'''
Object of a given class can invoke the methods available to it without revealing the implementation details to the 
user. 
Eg. We all have computer with us. Computer can be made using different components like Mouse, Keyboard, CPU, GPU,
Hard Disk, etc. and all these components have their own working. And computer is made by combining all 
these components together. So every component is a layer of abstraction.
'''

#   Encapsulation :
'''
Capsulating or putting all the variables, methods, functions inside a class is called Encapsulation.
Encapsulation hide the implementation details.
'''

# Modeling a problem in OPP's
'''
We identify following in our problem:
Noun --------->     Class  --------> Employee
Adjective ---->     Attributes ----> name, age, salary
Verb --------->     Methods  ------> getSalary(), incremnet()

# Class Attribute is the attribute that belongs to the class rather than a perticular object.

# Instance Attribute is the attribute that belongs to the Instance(object). 

'''

class RailwayForm:

    formType = "RailwayForm"

    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

HarrysApplication = RailwayForm()  #-----> Object Insantiation.
HarrysApplication.name = 'Harry'
HarrysApplication.train = 'Rajdhani Express'
HarrysApplication.printData()

class Employee:
    company = 'Google'  #-----> Class Attributes are those attributes which are belongs to the class 

harry = Employee()
rajni = Employee()
print(harry.company)
print(rajni.company)
Employee.company = "YouTube"  # -----> Change the class attribute value
print(harry.company)
print(rajni.company)



class Employee:
    company = "Google"
    salary = 100
maddy = Employee()
daddy = Employee()
maddy.salary = 300      #-----> Instance Attributes are those attributes which are belongs to the object
print(maddy.salary)
print(daddy.salary)
# Below line throws an error as address is not present in instance/class
print(maddy.address)


 
# ________________________X______________________ Self Function ________________________X_________________________

'''
It refers to the instance of the class. 
It is automatically passed with a function call from an object. 
When we use function inside a class we use self parameter. 

'''
class Employee:
    company = "Google"

    def getSalary(self):
        print(f'Salary is {self.salary}.')
        print(f"Salary for this employee working in {self.company} is {self.salary}.")

harry = Employee()
harry.salary = 100000

harry.getSalary()# ---> Equivalent to ---> Employee.getSalary(harry)


# ________________________X______________________ Constructor ________________________X_________________________
'''
- It belongs to the class argument. When you create a costructor, you have to put arguments in Class(). 
- "__init__()" is a special method which is first run as soon as the object is created. 
- '__init__' is also known as constructor.

 - Note* : __init__ runs automatically whenever function is instantiate (No need to call explicitly). 
'''

class Employee:
    company = "Google"

    def __init__(self, aname, asalary, asubunit):
        self.name = aname
        self.salary = asalary
        self.subunit = asubunit
        print("Employee is created.")

    def getDetails(self):
        print(f"The name of the Employee is {self.name}")
        print(f"The salary of the Employee is {self.salary}")
        print(f"The subunit of the Employee is {self.subunit}")

    def getSalary(self,signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}.\n{signature}")

harry = Employee("Harry",100,"You Tube")
harry.salary = 3000
harry.getSalary("Thanks")
harry.getDetails()



# ________________________X______________________ Static Method  ________________________X_________________________
'''
Sometime we need a function that doesn't use the "self" parameter.
We can define a static method like this:

                                    @staticmethod
                                    def greet():
                                        print('Good Morning Sir !')

"@staticmethod" is use to run the function without self attribute. 

'''
class Employee:
    company = "Google"
    def getSalary(self, signature):
        print(f'Salary is {self.salary}.\n{signature}')  

    @staticmethod
    def greet():
        print('Good Morning Sir !')

harry = Employee()
harry.salary = 100000
harry.getSalary("Thanks!")
harry.greet()   #----> it will run like ---> Employee.greet()




# ________________________X______________________ Class Method ________________________X_________________________
'''
A class method is a method which is bound to the class and not the object of the class.
It will change the "Class Attributes" not the instance attributes.

'''

class Employee:
    company = "***MiraInfoTech***"
    salary = 200
    location = "Delhi"

    @classmethod
    def changeSalary(cls,sal):
        cls.salary = sal

# ****** You can use this method also called " Dunder Class Method " mention below****
    # def changeSalary(self,sal):    
    #     self.__class__.salary = sal

e = Employee() 
print(e.company)
print(e.salary)
e.changeSalary(350)
print(e.salary)
e.changeSalary(550)
print(e.salary) 


# ________________________X______________________ Class Method as a Constructor________________________X_________________________


class Employee:

    def __init__(self, aname, asalary, arole):
        self.salary = asalary
        self.name = aname
        self.role = arole
    
    def print_details(self):
        return(f"Employee name is {self.name}. \nEmployee salary is {self.salary}. \nEmplyee role is {self.role}.")

    @classmethod
    def from_dash(cls,string):
        # params = string.split('-')
        # return cls(params[0],params[1],params[2])
        return cls(*string.split('-'))

emp3 = Employee.from_dash('ritesh-1800-Software Developer')

print(emp3.print_details())



# _______________________X____________ Public, Private & Protected (Access Specifiers)Variables _______________X_________________________
'''
- Public Variables: You can access these variale anywhere outside class.

- Protected Variables: You can access these variable for Base class and it is Derived class but it wouldn't use 
  by outside environment.

- Private Variables: Here python do  "Name_Mangling"  means you can't directly access that varible even by mistakely. 
  So to ensure that python does namemangling.

'''
class Employee:
    leaves = 8

    _protect = 9        # Protected variable(single underscore)

    __private = 85      # Private variable(double underscore)

    def __init__(self, aname, asalary, arole):
        self.salary = asalary
        self.name = aname
        self.role = arole
    
    def print_details(self):
        return(f"Employee name is {self.name}. \nEmployee salary is {self.salary}. \nEmplyee role is {self.role}.")

emp = Employee('Bhavik',15000, 'Web Developer')

print(emp._protect)     #------> To Access Protected variable

print(emp._Employee__private) #------> To Access Private variable (Name_mangling)