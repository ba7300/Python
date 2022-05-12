'''
                            * Function Catching in Python *

Assume that we are using a function which takes 3 seconds time to run. And the same function run multiple times in our
code so it makes program slow. To avoid this ambiguity we use "Function Catching". Cayching will store the value of
that function in the variable which stor in your device's memeory location and when the same function repeats it will 
take no time to execute that function.


'''

import imp
import time
from functools import lru_cache

@lru_cache(maxsize=3)         # when you set "max size" it will only cach letest 3 values of function 
def some_work(n):
    # some task taking n seconds
    time.sleep(n)
    return n

if __name__=="__main__":

    print("Now running some work")
    some_work(3)

    # some_work(6)
    # some_work(1)                  when you run function it will cach this values only so it will again take time.
    # some_work(9)

    print("Done...Calling again..")
    some_work(3)

    print("Called again")