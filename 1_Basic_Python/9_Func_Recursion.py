'''                                 Functions & Recursion  
'''


'''                                     Function
'''
# - A Function is a group of statements performing a specific task.
# - When program gets biggger in size and it's complexity grows, it gets difficult for a programmer to keep track on 
#   which piece of code is doing what.
# - A function can be reused by the programmer in a given program any number of times.
#   Types of function : 1) Built in fuction, 2) User define function


def greet():
    print("Hello")
    print("Good Morning")
greet()

def add(x,y): #Formal Argument
    c=x+y
    print(c)
add(2,3)   #Actual Argument

def addi(x,y):
    c=x+y
    return c
result=addi(2,3)
print(result)

def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d
result1,result2=add_sub(2,3)
print(result1,result2)

# X______________________X_________________________X____________________________X_____________________________X

'''
Position :
            You can not change the position of the formal argument and actual argument ie. position of both values
            should not be missplaced.
'''
def person(name,age):
    print(name)
    print(age)
person(24,"bhavik")  # it will give you error because postion is missplace

# X______________________X_________________________X____________________________X_____________________________X

'''
Key : To overcome this problem we us key.

'''   
def person(name,age):
    print(name)
    print(age)
person(age=24,name="bhavik")


#X______________________X_________________________X____________________________X_____________________________X

'''
Default :
            In this we make either one or both values as default values so if we forget to give actual argument it will
            automatically get the default vlue.
'''


def person(name,age=24):
    print("bhavik")
    print(24)
person("bhavik")     #it will automatically show your age as it is bydefault in pass statement
                     # if you put new age in the actual argument then it will over ride that means it will print
                     # updated or new written age

# X______________________X_________________________X____________________________X_____________________________X


"***Variable length***"
def sum(a, *b): # *b means it has multiple values
    c=a
    for i in b:
        c+=i
    print(c)
sum(5,6,8,9)


def sum(*b): # *b means it has multiple values, you can make c=0 also
    c=0
    for i in b:
        c+=i
    print(c)
sum(5,6,8,9)

# X______________________X_________________________X____________________________X_____________________________X
 

"keyword Variable length Argument"
def person(name, **data):  # Double* is use for fetching multiple keyword data
    print(name)
    print(data)


person("bhavik", age=24, city="Mumbai", mob=8436874)

"                   **OR**                          "

def person(name, **data):
    print("Name",":",name)
    for i,j in data.items():
        print(i,":",j)
person("bhavik", age=24, city="Mumbai", mob=8436874)


# X______________________X_________________________X____________________________X_____________________________X
"""
                                        **Decorators**   

    Using Decorators you can add extra features in the existing function without touching existing function or without
    modifying existing function.
"""

def div(a,b):
    print(a/b)

def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner
div=smart_div(div)
div(2,4)


# X______________________X_________________________X____________________________X_____________________________X


'''
                                         " Doc String "

Doc string are used to get the detailed information about function.
'''
# def function2(a,b):
#     """ This is a function which will calculate average of two numbers."""

#     avg = (a+b)/2
#     return avg
# print(function2.__doc__)     

"X______________________X_________________________X____________________________X_____________________________X"

"                                           Recursion                                                   "
# Recursion is a function which calls itself.
# It is used to directly use a mathematical formula as a function.
# Eg. factorial(n) = n * factorial(n-1) Or     n! = (n-1)! * n

# Let's see How it works :

'Eg.1 :'
def factorial(n):
    if n==1 or n==0:                    #-----> Base condition which doesn't call a function any further
        return 1
    else:
        return n * factorial(n-1)       #------> Function calling itself

'               Or                  '
'Eg.2 :'

# def addy(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n + addy(n-1)
# a = addy(3)
# print(a)

'''This works as follows:

factorial(4)
4 * factorial(3)
4 * 3 * factorial(2)
4 * 3 * 2 * factorial(1)
4 * 3 * 2 * 1 * [factorial retruned]
'''

'X______________________X_________________________X____________________________X_____________________________X'

"                                           Fibonacci Sequence :                                                                "
# 0 + 1 + 1 + 2 + 3 + 5 + 8 + 13 + 21 + 34 + 55 ....

def fibo(x):
    a = 0
    b = 1
    if x <= 0:
        print("invalid value, Enter a valid one!")
    elif x == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2, x):  # 2 elements are printed so 0 and 1 are already occupied now from index 2 start
            c = a+b
            a = b
            b = c
            if c > 100:
                break
            print(c)

x=int(input("How many numbers would you like to print?:"))
fibo(x)

