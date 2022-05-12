"Q1. Create a class C-2D vector and use it to create another class representing a 3D vector. "

# class C2dvec :
#     def __init__(self,i,j):
#         self.icap = i
#         self.jcap = j
    
#     def __str__(self):
#         return f"{self.icap}i + {self.jcap}j"

# class C3dvec(C2dvec):
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.kcap = k

#     def __str__(self):
#         return f"{self.icap}i + {self.jcap}j + {self.kcap}k"

# v2d = C2dvec(7,3)
# v3d = C3dvec(4,8,3)
# print(v2d)
# print(v3d)


'''Q2. Create a class Pets from a class Animal and further create  class Dog from  class Pets. Add a method Bark 
       to class Dog.
'''
# class Animal:
#     types = "Domestic Animals"

# class Pets(Animal):
#     species = "Small Cat"

# class Dog(Pets):
#     child = "Puppies"

#     @staticmethod
#     def bark():
#         print("Dog is Barking!")

# dg = Dog()
# a = dg.child
# print(a)


'''
Q3. Create a class Employee and add salary and increaments properties to it. Write a method salary_after_increment
    method with a @property decorator with a setter which changes the value of increment based on the salary.
'''
# class Employee:
#     salary = 1000
#     increment = 1.5

#     @property
#     def SalaryAfterIncrement(self):
#         return self.salary*self.increment
    
#     @SalaryAfterIncrement.setter
#     def SalaryAfterIncrement(self,sai):
#         self.increment = sai/self.salary

# e = Employee()
# print(e.SalaryAfterIncrement)
# print(e.increment)
# e.SalaryAfterIncrement = 2000
# print(e.increment)

'''
Q4. Write a class Complex to represent complex numbers, along with overloaded operators + and * which adds and
    multiplies them.
'''
## Multiplication Formula: (a+bi)(c+di) = (ac-bd) + (ad+bc)i

# class Complex:
#     def __init__(self,r,i):
#         self.real = r
#         self.imaginary = i

#     def __add__(self,c):
#         return Complex(self.real + c.real , self.imaginary + c.imaginary)

#     def __mul__(self,c):
#         mulReal = self.real * c.real - self.imaginary * c.imaginary   # (ac - bd)
#         mulImg = self.real * c.imaginary + self.imaginary * c.real     # (ad+bc)i
#         return Complex(mulReal, mulImg)
    
#     def __str__(self):
#         if self.imaginary<0:
#             return f"{self.real} - {-self.imaginary}i"
#         else:
#             return f"{self.real} + {self.imaginary}i"

 
# print(c1 * c2)

'''
Q5. Write a class vector representing a vector of n dimension. Overload the + and * operator which calculate the sum
    and the dot product of them.
'''

# class Vector:
#     def __init__(self,vec):
#         self.vec = vec

#     def __str__(self):
#         str1 = ""
#         indx = 0
#         for i in self.vec:
#             str1 += f" {i}a{indx} +"
#             indx +=1
#         return str1[:-1]

#     def __add__(self,vec2):
#         newlst = []
#         for i in range(len(self.vec)):
#             newlst.append(self.vec[i] + vec2.vec[i])
#         return Vector(newlst)

#     def __mul__(self,vec2):
#         sum = 0 
#         for i in range(len(self.vec)):
#             sum +=(self.vec[i] * vec2.vec[i])
#         return sum
    
#     #  "Q7." Answer 
#     def __len__(self):          
#         return len(self.vec)

# v1 = Vector([1,4,3,7])
# v2 = Vector([1,6,2,8])
# print(v1+v2)
# print(v1*v2)
# print(len(v1))
# print(len(v2))


'''
Q6. Write __str__() method to print the vector as follows:
    7^i + 8^j + 10^k
    Assume vector of dimension 3 for this problem.
'''
# class Vector:
#     def __init__(self,vec):
#         self.vec = vec

#     def __str__(self):
#         return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"

# v1 = Vector([1,4,6])
# v2 = Vector([1,6,9])
# print(v1)
# print(v2)



