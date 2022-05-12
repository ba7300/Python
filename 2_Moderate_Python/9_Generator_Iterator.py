

#                                               Iterator

'''
Iterable - when you run "__iter__()" or "__getitem__()" method on object, it will give you Iterator.

Iterator - It is an object in which "__next__()" method is defined & it will provide it's next item.

Iteration is the Process of iterating an object.

Eg. : 
      If I want to traverse a Python object like a list or string, etc. and if I try to access that object in FOR Loop,
      I can access it or not will decide by if that object is iterable or not.

      If the object is Iterable then I can Iterate that object.
      Now if it is iterable then how can I iterate it? 
      So it will run the "__iter__()" function and create/generate Iterator.
      And when we run the '__next__()' method  on iterator, it will provide it's next item..

      String is an iterable. In string "__iter__()" item is defined so u can iterate it directly. 
'''

h = "Bhavik"
# for c in h:
#     print(c)

element = iter(h)  # created 'element' object as iterator

print(element.__next__())
print(element.__next__())
print(element.__next__())
print(element.__next__()) 

# But if I use
h = 7300
# and try to run it will throw an error : TypeError: 'int' object is not iterable



#                                               Generators 
'''
          - Generators are a type of Iterators("__next__()"). 

          - It is a type of Iterator which you can traverse(iterate) only once and it doesn't repeat.
          
          - Genrator generates values on the fly.

          - For eg. If I want to execute this number 3435454364575434 and if I put it in range function like below:

                    for i in range(3435454364575434):
                      print(i)
       So range will not executed that number at that moment, actually it will execute that number on the fly when the
       function runs.

          - We use generator to save the RAM. If I don't want to store (3435454364575434) such a large number in my 
            memory and make my system slow then I will use generator.

          - Here what I did is, I have created a generator which is capable of generating numbers from 0 to 3435454364575434 
            but I don't want to execute that number now, neither want to store that number in RAM, so I just make it 
            ready and whenever I required that number I will Iterate it. 

            *Note : 'Range' is also a Generator.
'''

# Create a Generator:

from operator import ge


def gen(n):
    for i in range(n):
        yield i         # Here, Yield is a generator, it will generate values on the fly.
g = gen(34354543645746655434)
print(g)


" Now I will prove : Generators are type of Iterators which do not repeat."
g = gen(3)                 
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())       # This line will throw an error because Iteration limit is exceeded 
# print(next.g)

for i in g:             # but FOR loop is designed in such a way that it will handele the 'stop Iteration' automatically.
    print(i)





"_______________X_______________X_________________X__________*  EXERCISE *__________X________________X______________X"


# Eg.1 :

def factorial(n):
    sum = 1
    for i in range(n, 0, -1):
        sum = sum * i
    yield sum

def fibonacci(nterms):
    n1, n2 = 0, 1
    for i in range(nterms):
        yield n1
        nth = n1 + n2
        n1 = n2
        n2 = nth
'X_______________________________X________________________________X'
# Eg.2 :

a = int(input('Give amount: '))

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(tuple(fib(a)))