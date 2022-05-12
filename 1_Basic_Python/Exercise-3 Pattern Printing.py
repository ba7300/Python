

print('# Pattern Printing #')


n = int(input("How many rows do you want to print: "))
print("Enter 1 or 0 ")
bool_val = input("Enter 1 for True OR 0 for false: ")
if bool_val=='1':

        for i in range(n):
            for j in range(i+1):
                print('*',end='')
            print()
else:
    for i in range (n):
        for j in range(n-i):
            print('*', end='')
        print()

