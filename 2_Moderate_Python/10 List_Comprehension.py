'''
_______X_______X__________X__________X_______* List Comprehensions in Python *_______X_______X__________X__________X


- List comprehension is an elegant way to creates lists based on existing list.
   
Eg.       lst1 = [1,7,12,11,5]

        lst2 = [item for item in lst1 if item>8]
'''


a = [17,9,10,21,16,18,19,95,90,94,91]
b = []
for i in a:
    if i % 2 == 0:
        b.append(i)
print(b)

# # Shortcut to write the same :

c = [i for i in a if i%2==0]
print(c)

"_______X_______X__________X__________X______* Dictionary Comprehensions in Python *_______X_______X__________X________X"


dict1 = {i:f"Item-{i}" for i in range(5)}
print(dict1)

# Reverse the dictionary

re_dict1 = {value:key for key,value in dict1.items()}
print(re_dict1)


"_______X_______X__________X__________X_______* Set Comprehensions in Python *_______X_______X__________X__________X"

# dresses = {dress for dress in ['dress1','dress2','dress1','dress2','dress1','dress2']}
# print(dresses)



"_______X_______X__________X__________X_______* Generator Comprehensions in Python *_______X_______X__________X__________X"

evens = (i for i in range(100) if i%2==0)
print(type(evens))
print(evens)
# print(evens.__next__())
# print(evens.__next__())
# print(evens.__next__())

for item in evens:
        print(item)