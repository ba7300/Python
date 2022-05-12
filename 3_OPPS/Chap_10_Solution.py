'Q1. Create class programmer for storing information of few programmers working at Microsoft.'

# class Programmer:
#     company = "Microsoft"

#     def __init__(self, name, product):
#         self.name = name
#         self.product = product

#     def Info(self):
#         print(f"The name of the {self.company} Programmer is {self.name} and the product is {self.product}.")

# Vikesh = Programmer('Vikesh', 'GitHub')
# Ritesh = Programmer('Ritesh', 'Skype')
# Vikesh.Info()
# Ritesh.Info()

"Q2. Write a class calculator capable of square, cube & square root of a number."

# class Calculator:
#     def __init__(self,num):
#         self.num = num
        
#     def sqaure(self):
#         print(f"The valu of {self.num} square is = {self.num**2}.")
#     def cube(self):
#         print(f"The valu of {self.num} cube is = {self.num**3}.")
#     def sqaureRoot(self):
#         print(f"The valu of {self.num} squareRoot is = {self.num**0.5}.")

# a = Calculator(4)
# a.sqaure()
# a.sqaureRoot()
# a.cube()

'''Q3. Create a class with a class atribute 'a', create an object from it and set 'a' directly using object a=0. 
       Does this change the class atribute?'''

# class Sample:
#     a = "Dhiraj"

# obj = Sample()
# obj.a = "Viky"

# print(Sample.a)
# print(obj.a)

'''Q4. Add a static method in (Q.2) to greet the user with "Hello".
'''
# class Calc:
#     def __init__(self,num):
#         self.num = num
#     def Square(self):
#         print(f"The value of {self.num} Square is = {self.num**2} ")
#     def Cube(self):
#         print(f"The value of {self.num} Cube is = {self.num**3} ")
#     def SquareRoot(self):
#         print(f"The value of {self.num} SquareRoot is = {self.num**0.5} ")

#     @staticmethod
#     def greet():
#         print("Thank You!")
# a = Calc(4)
# a.Square()
# a.SquareRoot()
# a.Cube()
# a.greet()

'''Q5. Write a class Train which has method to book a ticket, get status(no. of seats) and get fare information of 
       trains running under Indian Railway.'''

# class Train:
#     def __init__(self, name, fare, seats):
#         self.name = name
#         self.fare = fare
#         self.seats = seats

#     def getStatus(self):
#         print(F"The name of the train is {self.name}")
#         print(f"The seats available in train are {self.seats}")

#     def fareInfo(self):
#         print(f"The fare of the ticket is: {self.fare}")
    
#     def bookTicket(self):
#         if (self.seats > 0):
#             print(f"Your seat has been booked! Your seat number is {self.seats}")
#             self.seats -= 1
#         else:
#             print(f"Sorry this train is full! Kindly try in Tatkal.")

#     def canceTicket(self, seatNo):
#         pass

# intercity = Train('Intercity:1405', 110, 2)
# intercity.getStatus()
# intercity.farInfo()
# intercity.bookTicket()