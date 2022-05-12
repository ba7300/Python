'''
Q.2) Write a program to input name, marks and phone number of a student and format it using the format function like
     below:
    " The name of the student is Harry, his marks are 73 and phone number is 8329789693"
'''

name = input("Enter your name: ")
marks = int(input("Enter marks: "))
phone_number = int(input("Enter phone number: "))

Template = "The name of the student is {2}, his marks are {0} and phone number is {1}.".format(marks,phone_number,name)

print(Template)


'''
Q.3) A list contain multiplication table of 7. Write a program to convert it to a vertical string of same
     numbers (7..14...)
'''
num = int(input("Enter a number: "))
lst = [str(num*i) for i in range(1,11)]
op = '\n'.join(lst)
print(op)


" Q.4) Write a program to filter a list of numbers which are divisible by 5.    "

l = [17,34,45,23,10,7,18,21,90,55,43,67,88,25,12,33,15]

a = filter(lambda a: a % 5 == 0, l)
print(list(a))


" Q.5) Write a program to find the maximum of the numbers in a list using reduce function.  "

from functools import reduce

l = [17,12,10,18,21,16]

a = reduce(max,l)
print(a)