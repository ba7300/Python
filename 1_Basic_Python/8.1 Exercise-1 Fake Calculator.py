'''
                        ***          Fake Calculator            ***
                        
    - Design a calculator which correctly solve all the problems except the following once:
    - 45 * 3 = 555, 56 + 9 = 77, 56 / 6 = 4
    - Your program should take operator and two numbers as input from the user and then return the result.
'''

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

c = input("Please type the math operation you would like to perform:"
" Choose (+)  For Addition,"
" Choose (-)  For Subtraction,"
" Choose (*)  For Multiplication"
" Choose (/)  For Division,"
" Choose (**) For Power,"
" Choose (%)  For Module:  ")

if a==45 and b==3 and c=='*':
    print(555)
elif a==56 and b==9 and c=='+':
    print(77)
elif a==56 and b==6 and c=='/':
    print(4)
elif c =='+':
    d = a+b
    print(d)
elif c =='-':
    d = a-b
    print(d)
elif c =='*':
    d = a*b
    print(d)
elif c =='/':
    d = a/b
    print(d)
elif c =='**':
    d = a**b
    print(d)
elif c =='%':
    d = a%b
    print(d)