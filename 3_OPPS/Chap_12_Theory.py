
                                        # Chapter 11:- Polymorphism
                                        
'''
Defination :-
              Polymorphism means ablity to take various forms( Or One thing behave in different ways).

              If we breakdown this word "Polymorphism" then 'Poly' means 'MANY' / 'MULTIPLE'  and 'MORPH' means 'FORMS', 
              so all together it becomes "*Multiple Forms*" of same object. It can be 'Atributes' or 'Methods'.

              Eg. : 
              - As a Human we behave differently in offiece, at home we behave differently and when we are with our
                friends our behaviour changes. 
              - So we have defferent forms depends on the situation, as situation changes we change our behaviour too. 
              - In the same way when we can talk about objects, objects have multiple forms.

'''

#"________________________X______________________ Operator Overloading ________________________X_________________________"

" Operator Overloading in Python :- Operators in python can be overloaded using dunder methods. "
" This method is called when a given operator is used on the objects."                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    

class Employee: 

    def __init__(self, aname, asalary, arole):
        self.salary = asalary
        self.name = aname
        self.role = arole
    
    def print_details(self):
        return(f"Employee name is {self.name}. \nEmployee salary is {self.salary}. \nEmplyee role is {self.role}.")

    def __add__(self,others):
        return self.salary + others.salary
    
    def __truediv__(self,others):
        return self.salary / others.salary

    def __repr__(self):
        # return self.print_details
        return(f"Employee ('{self.name}', '{self.salary}', '{self.role}')") 

    def __str__(self):
        return(f"Employee name is {self.name}. \nEmployee salary is {self.salary}. \nEmplyee role is {self.role}.")

emp1 = Employee('Bhavik',60, 'Programmer')
# emp2 = Employee('viky',70,'Junior Engineer')

# print(emp1 + emp2)
# print(emp1 / emp2)

print(emp1)                # It will always give "__str__" method 1st preference, 
print(repr(emp1))          #  unless and until you explicitely mention other method.  

#----------------------------------------------------------------------------------------------------------------------

class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self,num2):
        print("Let's Add")
        return self.num + num2.num

    def __mul__(self, num2):
        print("Let's Multiply")
        return self.num * num2.num

n1 = Number(4)
n2 = Number(6)

sum = n1 + n2
print(sum)
mul = n1 * n2
print(mul)


#X_____________X______________X_______Absract Base class(ABC) & @abstractmethod __________X_______________X________________X
'''
When you inherites any class as a "ABC Metaclass" then that class can order their child classes to strictly implement
some methods othervise they will get an error.

In this method we create a "Base class(Parent class)" which imposes rules or sends orders to it's" Child class".
In other words, the ABC Metaclass class forces its child classes to implement the methods mentioned in ABC Metaclass
else it shows an error.

*Note : You can't create object directly from ABC Metaclss.

'''

# from abc import ABCMeta, abstractclassmethod  #(for Old Versions)

# class Shape(metaclass = ABCMeta):     #(for Old Versions)

from abc import ABC, abstractclassmethod      #(For New Versions)

class Shape(ABC):

    @abstractclassmethod    
    def printarea(self):   # It say's, you must use "Printarea()" in every class you will inherit from this class.
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4

    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printarea(self):
        return self.length * self.breadth

rect1 = Rectangle()

"# rect2 = Shape() ---->   This will throw error because You can't create object directly from ABC Metaclss."
print(rect1.printarea())




#X________________X_________ Property Decorators : @getter and @setter and @deleter __________X_______________X


#_____________________________________________ STEP: 1 ______________________________________________

class Employee:

    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithharry.com"   


    def explain(self):
        return f"This employee is {self.fname} {self.lname}"  
  

# emp1 = Employee("Hindustani","Supporter")

# print(emp1.explain())
# print(emp1.email)

    "Now if 'emp1' want to change emp1's fname,he can change it  but the email won't change. It remain as it is."

# emp1.fname = "US"
# print(emp1.email)


    "To overcome this problem 1st we need to create a email function"
#_____________________________________________ STEP: 2 ______________________________________________

#     def email(self): 
#         return f"{self.fname}{self.lname}@codewithharry.com"

# emp1 = Employee("Hindustani","Supporter")

# emp1.fname = "US"
# print(emp1.email())


    "To access email function as a property we use @property decorators"
#_____________________________________________ STEP: 3 ______________________________________________

    # @property
    # def email(self): 
    #     return f"{self.fname}.{self.lname}@codewithharry.com"


# emp1 = Employee("Hindustani","Supporter")

# emp1.fname = "US"
# print(emp1.email)

    "Now if I try to change email directly,it shows an Error - AttributeError: can't set attribute."
# emp1.email = "Bhavik.Tandel@CodewithHarry.com" 
# print(emp1.email)

    ''' To overcome this problem we use "Setter" which will set this attribute.'''
#_____________________________________________ STEP: 4 ______________________________________________

    # @email.setter
    # def email(self,str):
    #     names = str.split('@')[0]
    #     self.fname = names.split('.')[0]
    #     self.lname = names.split('.')[1]

# emp1 = Employee("Hindustani","Supporter")

# emp1.fname = "US"
# print(emp1.email)
# emp1.email = "Bhavik.Tandel@CodewithHarry.com"
# print('\n',emp1.email)


    ''' Now if I want to Delete above email I will write :   "del emp1.email"    # It will show an Error: "You can't delete this attribute"            
        To overcome this problem we need to create "Deleter".'''    
#_____________________________________________ STEP: 5 ______________________________________________

    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return "Email is not set. Please set it using setter." 
        return f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter
    def email(self,str):
        names = str.split('@')[0]
        self.fname = names.split('.')[0]
        self.lname = names.split('.')[1]

    @email.deleter                                              
    def email(self):
        self.fname = None
        self.lname = None


emp1 = Employee("Hindustani","Supporter")

emp1.email = "Bhavik.Tandel@CodewithHarry.com"
print('\n',emp1.email)

del emp1.email
print('\n',emp1.email)

emp1.email = "Harry.Parry@CodewithHarry.com"
print('\n',emp1.email)



#X_______________________X______________________ Object Introspection _____________________X_________________________X

'Object Introspection means to get the information about object.'

o = 'My name is Bhavik'

print(type(o))
print(id(o))

print(dir(o))
print(dir(emp1))

import inspect
print(inspect.getmembers(emp1))


# X_______________________X______________________ Duck Typing _____________________X_________________________X
'''
We have a famous line: If there is a bird, which is walking like a duck, which is quacking like a duck and which is 
swimming like a duck, that bird shoul be a duck.

"If it looks like a duck, swims like a duck and quacks like a duck then it probably is a duck."

It doesn't matter if it is Duck or not what matters is, it behaves like a Duck. It's behaviour is important.

'''

class Pycharm:
    def execute(self):
        print('Compiling')
        print('Running')

class Mycharm:
    def execute(self):
        print('Spell Check')
        print('Convention Check')
        print('Compiling')
        print('Running')

class Laptop():
    def code(self,ide):
        ide.execute()
    
# ide = Pycharm()
ide = Mycharm()      # So it doesn't matter which class object you are passing, what matters is that object should 
                     # have "execute" method.
Lap1 = Laptop()
Lap1.code(ide)