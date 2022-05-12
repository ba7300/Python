'''
if __name__ == "__main__" in python:-

- __name__ evaluates to the name of the module in Python from where the program is ran.

- If the module is being run directly from the command line, the __name__ is set to string "__main__". Thus this
  behaviour is used to check wheether the module is run directly or imported to another file.
'''

def greet(name):
    print("Good Morning, ",name)
print(__name__)                   #-----> It will give you name of the file i.e. " m05_file_1 "


if __name__ == "__main__":

    n = input("Enter the name: ")
    greet(n)