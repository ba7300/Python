'''
Q.1) Write a program to open three files 1.txt, 2.txt & 3.txt. If any of these files are not present, a message without
     exiting the program must be printed prompting the same.
'''

# with open('1.txt','w') as f:
#     f.write(" Hi! This is file One.")

# with open('2.txt','w') as f:
#     f.write(" Hi! This is file Two.")

# with open('3.txt','w') as f:
#     f.write(" Hi! This is file Three.")


def readFile(filename):
    try:
        with open(filename) as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File {filename} is not found...!")

readFile('chap12_1.txt')
readFile('chap12_2.txt')
readFile('chap12_3.txt')


"Q.2) Write a program to print 3rd, 5th and 7th elemnt from a list using enumerate function.    "

lst1 = [17, 10, 21, 16, 9, 18, 95,19,90, 64]

for index, item in enumerate(lst1):
    if index == 2 or index == 4 or index == 6:
        # print(index,item)
        print(f"The {index+1}th element is: {item} ")


"Q.3) Write a list comprehension to print a list which contains the multiplication table of a user entered number.  "


Numb = int(input("Enter a number: "))

Table = [Numb*i for i in range(1,11)]
print(Table)


"Q.4) Write a program to display 'a/b' where a & b are integers. If b=0, display infinite by handling the ZeroDivisionError   "

a = int(input("Enter  number 1: "))
b = int(input("Enter  number 2: "))

try:
    print(a/b)
except:
    print("Infinite!!")

    
    
"Q.5) Store the multiplicwtion tables generated in problem 3 in a file named Tables.txt "

num = int(input("Enter a numbeer: "))

tables = [num*i for i in range(1,11)]
print(tables)
with open("chap12_tables.txt",'a') as f:
    f.write(str(tables))
    f.write('\n')