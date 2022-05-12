'''                 **    Map    **

Map : It applies the function on all the elements present in the existing list and create new list.



Syntax :         _______>(can be lambda function)
                |
        map(function, input_list)
''' 
# Map :

# Method 1
def sqr(num):
    return num*num

lst1 = [2,4,3,5]
lst2 = []
for item in lst1:
    lst2.append(sqr(item))
print(lst2)

"Instead of typing above code I will use MAP method"

# Method 2
print(list(map(sqr,lst1)))

# Method 3
print(list(map(lambda n:n*n,lst1)))


'''
                **      Filter      **
 : Filter creates a list of elements for which the function returns True.

            list(filter(function,l))
                            |_________>(can be lambda function)
'''

def greater_than_5(num):
    if num > 5 : 
        return True
    else: 
        return False


lst = [17,5,19,3,10,3,21,2,18,8,6,9,7]

print(list(filter(greater_than_5,lst)))

g10 = lambda num : num>10
print(list(filter(g10,lst)))

#                       OR

num = [2,7,4,76,45,89,31,34,17,21,10,22,18]

print(list(filter(lambda n: n%2==0,num)))



'''
                **      Reduce      **

Reduce applies a rolling computation to sequential pair of elements.
'''

from functools import reduce

l = [1,2,3,4]
sum = lambda a,b : a+b

val = reduce(sum,l)
print(val)

#           OR

val2 = reduce(lambda a,b:a+b,l)
print(val2)