'''
                                    Array in Python          

Array is a data structure that store values of same data type.
List can contain  values corresonding to different data types. 
Array in python can only contains value corresponding to same data type.                 
'''


# from array import *

# br = array('i',[17,10,9,16,21,8,18])

# # cr = array('u',['b','h','a','v','i','k'])

# print(type(br))
# print(br)
# print(br.buffer_info())

# NewArr = array(br.typecode, (a*a for a in br))
# for e in NewArr:
#     print(e)

"X----------------X--------------------X------------------------X--------------------X"

'''
                                    Numpy Operations


In Python, array package doesn't support Multidimensional or Multiple Arrays.So we need to use 3rd party package 
here called " Numpy ".

'''
from numpy import *

arr2 = array([17,5,19,95.0])
print(arr2.dtype)
print(arr2)

arr3 = array([17,5,19,95],float)
print(arr3.dtype)
print(arr3)


"""                                          linspace()
"""
# Break the value into number of parts, takes 3 parameters for eg.('start', 'stop','no. of parts')

arr4 = linspace(0,15)               # Divide into 50 parts by default.
arr4 = linspace(0,15,16)            # Divide into 16 equal parts
print(arr4)


"""                                           arange()
"""
# It works same like range function and it creates array.

arr5 = arange(1,15,2)
print(arr5)


"""                                           logspace()
"""
#Give the log value.

arr6 = logspace(1,40,5)
print(arr6)
print('%.2f'%arr6[1])


"""                                           zeros() & ones()
"""

arr7 = zeros(5)     #  arr7 = zeros(5,int)
print(arr7)

arr7 = ones(5)      # arr7 = ones(5, int)
print(arr7)


"X----------------X--------------------X------------------------X--------------------X"

'                               "Basic Operations"                          '
arr1 = array([1,2,3,4,5])
arr2 = arr1 + 5
print(arr2)                 # o/p : [6,7,8,9,10]

print(concatenate([arr1,arr2]))     # o/p : [1,2,3,4,5,6,7,8,9,10]


arr3 = arr1 + arr2                  # This is also called *Vectorize Operation*/ addition of 2 arrays
print(arr3)

# print(sin(arr1))
# print(cos(arr1))
# print(log(arr1))
# print(sqrt(arr1))
# print(sum(arr1))
# print(max(arr1))
# print(min(arr1))
# print(sort(arr1))

"X----------------X--------------------X------------------------X--------------------X"


#                            How to copy an Array in Numpy ?
'''
    There are two methods which are used to copy an array :
                     1) Shallow copy 
                     2) Deep copy

1) Shallow Copy: 
                In this method the value of 2nd array is depend on 1st array i.e if you make any changes in 1st  
                array it will directly affect the 2nd array (The vlaue of 2nd array also change).

'''
arr1 = array([2,6,8,1,3])
arr2 = arr1.view()  

arr1[1]=10

print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))

'''
2) Deep Copy: 
             In this method the value of 2nd array is not dependent on 1st array i.e changes in 1st array will not
             reflect in the 2nd array.
'''
arr1 = array([2,6,8,1,3])
arr2 = arr1.copy()

arr1[1]=10

print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))

"X----------------X--------------------X------------------------X--------------------X"


"                               Working with MATRIX in Python                                           "

arr1 = array([

    [1,2,3,6,2,9],
    [4,5,6,7,5,3]
])

# print(arr1)
# print(arr1.dtype)                 # Data type
# print(arr1.ndim)                  # Number of dimensions
# print(arr1.shape)                 # Give no. of Rows & Columns
# print(arr1.size)                  # Give size of the entire block


"Convert 2D to 1D array"

arr2 = arr1.flatten()
# print(arr2)


"Convert Singledimensional Array to Multidimensional Array"

# arr3 = arr2.reshape(3,4) # (Rows, Columns)

arr3 = arr2.reshape(2,2,3)                          # (Two 2d array, each has 2 1d array, each 1d has 3 values)
print(arr3)


