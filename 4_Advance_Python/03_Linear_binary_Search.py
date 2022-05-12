'''
                                            Linear & Binary Search
'''
#   Linear Search :

# from operator import truediv


# lst = [5,8,4,6,9,17]
# # n = 17
# n=int(input('enter a number'))
# for i in range(len(lst)):
#     if lst[i]==n:
#         print('found at pos',i+1)
#         break
# else:
#         print('not found')

'''                                           Binary Search  
'''
pos = -1

def search(lst,n):

    l = 0
    u = len(lst)-1

    while l <= u:
        mid = (l+u)//2

        if list[mid] == n:
            globals() ['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid+1
            else:
                u = mid-1
    return False

lst = [5,8,4,6,9,17]
n = 17

if search(lst, n):
    print('found at', pos+1)
else:
    print('not found')

# ----------------X-------------------- Telusko -------------------X-------------------#


"                               **************** Linear search *********************                                    "

Position=-1
def search(List,n):
    i=0
    while i< len(List):              #   for i in range(len(List)):
        if List[i]==n:               #       if List[i]==n:
            globals()['Position']=i  #           globals()['Position']=i
            return True              #           return True
        i+=1                         #   return False
    return False                     #


List=[ 17,5,19,95,10]
n=17

if search(List,n):
    print("Found at Position",Position+1)
else:
    print("Not Found")

''' 
                              **************** Binary search *********************                                        


In binary search your mid value changes depends on the range of expected value , initially your lower value must be 0
and uppper value must be max value of the list and youe mid value is (lower + Upper)/2, and
if your search value is less than mid value then you will replace the upper value at mid value position and
your mid value becomes your new upper value and vice versa.

'''
Pos=-1

def search(List,n):
    l=0
    u=len(List)-1
    while l<=u:
        mid=(l+u)//2
        if List[mid]==n:
            globals()['Pos']=mid
            return True
        else:
            if List[mid] < n:
                l=mid+1
            else:
                u=mid-1
    return False

List=[1,2,4,7,9,10,16,17,21,1962,1964,1990,1995]
n=17

if search(List,n):
    print('Found at',Pos+1)
else:
    print("Not Found")


"                               **************** Bubble Sort  *********************                                         "

def sort(nums):
    for i in range(len(nums)-1,0,-1): # it check the no. of elements you have
        for j in range(i):             # it is use for swapping
            if nums[j]>nums[j+1]:
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp


nums=[5,3,8,6,7,2]
sort(nums)

print(nums)

"                               **************** Selection Sort  *********************                                      "

# It does lot of swapping so to avoid that we use this method we swap at once.

def sort(nums):
    for i in range(5):
        minpos=i
        for j in range(i,6):
            if nums[j]<nums[minpos]:
                minpos=j
        temp=nums[i]
        nums[i]=nums[minpos]
        nums[minpos]=temp
        print(nums)

nums=[5,3,8,6,7,2]
sort(nums)

print(nums)

