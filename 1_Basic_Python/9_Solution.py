'Q1. Write a program using function to find greatest of three numbers.'

# def max_num(num1, num2, num3):    | def greatest_integer(n1,n2,n3):
#                                   |
#     if num1>num2:                 |     if n1>n2 and n1>n3: return n1  
#         if num1>num3:             |     elif n2>n3: return n2  
#             return num1           |     else: return n3
#                                   |
#         else: return num3         | op = greatest_integer(17,5,19,95)
#                                   | print(op)       
#     else:                         |        
#         if num2>num3:             |
#             return num2           |
#         else: return num3         |
#                                   |
# m = max_num(17,5,95)
# print(m)

'''____________________________'''

'Q2. Write a python program using function to convert celsius to fahrenheit.'

# def farh(cel):
#     return(cel*(9/5))+32
# c = 45
# f= farh()    
# print("Fahreheit Temperature is : ",f)

'''____________________________'''

'Q4. Write a recursive function to calculate the sum of first n natural numbers.'

# def natnum(n):
#     if n==1: return 1
#     else:
#         return n + natnum(n-1)
# a = natnum(5)
# print(a)

'''____________________________'''


"  Star Pattern"
n = int(input("Enter the number : "))

for i in range(n):
    print("*" * (n-i))

'''____________________________'''

'Q5. Write a python function to remove a given word from a string and strip it at the same time.'

# def rem_and_strp(string,word):
#     newStr = string.replace(word,'')
#     return newStr.strip()

# this = '      Harry is a good teacher      '
# n = rem_and_strp(this, 'Harry')
# print(n)