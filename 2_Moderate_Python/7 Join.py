'''Join Function :- Create a string from iterable objects'''

l = ['Camra','Laptop','iPad','Hard Disk','Power Bank']

sentence = '_and_'.join(l)
# sentence = '=='.join(l)
# sentence = '~~'.join(l)
# sentence = '\n'.join(l)
print(sentence)
print(type(sentence))

''' 
                $ Format Method $
                
- It was use before f'string method.
Eg. 
''' 
n = 'Harry'
c = 'CodeWithHarry'
t = 'coding'

    # In F'String we use : a = f"This is {n} and his channel is {c}"
    
    #   In Format Method :
a = "This is {} and his channel is {}".format(n, c)
    # OR
a = "This is {1} and his {2} channel is {0}  ".format(n, c, t)

print(a)
