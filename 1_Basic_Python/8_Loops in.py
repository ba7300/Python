'Q1. Write a program to print multiplication table of a given number using For Loop.'

# num = int(input('Enter the number :'))
# for i in range(1,11):
    
#     print(i,'X',num, '=',num*i) 
#                   Or
#     print(f"{num} X {i} = {num*i}")   

# ---------------****  OR Using While Loop ****----------------------------

# num = int(input('Enter the number :'))
# i=1 
# while i <= 10:
#     print(f"{num} X {i} = {num*i}")
#     i +=1

# ----------------------*** Reverse Order Table ****--------------------

# num = int(input('Enter the number :'))
# for i in range(10,0,-1):
#     print(f"{num} X {i} = {num*i}")


'''Q2. Write a program to greet all the program names stored in a list 'L1' and which starts with "R".
       L1 = ['Ramesh','Suresh','Ritesh','Rakesh','Rupesh','Vikesh','Haresh']
'''

# l1 = ['Ramesh','Suresh','Ritesh','Rakesh','Rupesh','Vikesh','Haresh']
# for name in l1:
#     if name.startswith('R'):
#         print('Hello, ',name + '!')
# print('You all are selected, Congratulations.')


"Q4. Write a program to find out wether a given number is prime or not. "

# num = int(input('Enter the number :'))
# for i in range(2,num):
#     if num%i == 0:
#         print(num,' is not a prime number.')
#         break
# else: print(num,' is a Prime number')


'Q5. Write a program to find the sum of first n natural numbers using While Loop.'

# num = int(input('Enter the number :'))
# i=1
# v=0
# while i <= num:
#     v = v+i
#     i+=1
# print('Sum of Number',num,'is =',v)


'Q6. Write a program to calculate the factorial of a given number using For Loop.'

# num = int(input('Enter the number :'))
#fac = 1
# for i in range(1,num+1):
    # fac = fac*i
# print(f"The Factorial of {num} is {fac}.")

    
'Q7. Write a program to print following Pattern:  star Pyramid.'

# n=5
# for i in range(n):
#     for j in range(n-i):
#         print(' ',end='')
#     for k in range(i+1):
#         print('* ',end='')
#     print()