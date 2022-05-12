'''
        * Enumerate Function *

It adds counter to an iterable and returns it.  (Inshort it gives Index value of the elemets)

Eg.     for index,item in list1:
            print(item,index) ------> Print items of list1 with index!
'''
# Eg.1:-

list1 = [17, 5, 19, 'Harry', True, 73]

# index = 0
# for i in list1:
#     print(i, index)
#     index += 1

for index, i in enumerate(list1):
    print(i,index)
    print(f"index of {i} is {index}")


# Eg.2 :-

l1 = ['Bhindi', 'Aloo','Chopsticks', 'Chowein']
# i = 1
# for item in l1:
#         if i%2 is not 0:
#                 print(item)
#         i +=1

for index,item in l1:
        if index % 2 is 0:
                print(f"Jarvis please buy {item}")