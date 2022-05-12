'''
            * The Global Keyword *

It is used to modify the variable outside of the current scope.
'''


a = 17                                  # Global

def func1():
    global a
    print(f"Print statement 1: {a}")

    a = 73                               # Local variable if global is not used
    print(f"Print statement 2: {a}")

func1()
print(f"Print outside function : {a}")

'''
                        Telusko Notes
'''
a=10

def something():
    a=9                         #  u can mention global variable inside the function by explicitly denoting"global a"
    print("Local:",a)           #    Local variable get 1st preference
something()
print("Global:",a)              #    Global variable gets 2nd preference