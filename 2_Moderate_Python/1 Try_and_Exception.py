
                # Exception Handling in Python:

'''
An exception is an unusual condition that results in an interruption in the flow of the program.
When the try block throws an error, the control goes to the except block.

- Exception in Python can be handled using a "try" statement.
- The code that handles the exaception is written in the "except" clause.
- There are many built-in exceptions which are raised in python when something goes wrong.


- Eg. '''
try:
    a=0
            # Code              --------> Code which might throw an exception
            
except exception as e:
            print(e)


"- When the exception is handled, the code flow continues without program interruption."


while(True):
    print("Press q to quit")
    a = input("Enter a Number: ")

    if a == "q":
        break
    try: 
        a = int(a)
        if a> 5:
            print("You Entered a number greater than 5")

    except Exception as e:
        print(f"Your input resulted in an Error: {e}")

print("Thanks for playing the game!")

# ----------------X--------------------#-------------------X-------------------#


                    # Handling Different Excepptions in Python

try:
    a = int(input("Enter a number: "))

    c = 1/a
    print(c)

except ZeroDivisionError as e:
    print("Make sure you are not dividing by 0.")

except ValueError as e:
    print("Please enter a valid value.")

print("Thanks for using this code!")

# ----------------X--------------------#-------------------X-------------------#


                    # Customize/Modify an Exception in Python
'''
We can custom exceptions using the raise keyword in python.
'''

def increament(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("This is not good - Harry!")

a = increament('gf73')
print(a)

# ----------------X--------------------#-------------------X-------------------#

                            # *Try With Else*

'''
        Sometimes we want to run a piece of code when try is successful.

Eg.
    try:
        # Some Code
    except:
        # Some Code
    else:
        # Code       ----------> This is executed only when the try gets successful.
'''
try:
    i = int(input("Enter a number: "))
    c = 1/i
except Exception as e:
    print(e)
else:
    print("We were Successful...")

# ----------------X--------------------#-------------------X-------------------#


                        #   *Try With Finally*

'''
        Python offers a finally clause which ensures execution of a piece of code irrespective of the exception.

Eg.
    try:
        # Some Code
    except:
        # Some Code
    finally:
        # Code       ----------> This executed regardless of Error!
'''
try:
    i = int(input("Enter a number: "))
    c = 1/i
except Exception as e:
    print(e)
    exit()
finally:
    print("We are Done...")

print('Thanks for using the program.')