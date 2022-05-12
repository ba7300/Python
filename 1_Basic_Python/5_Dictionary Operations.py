"             *********Dictionary in Python***********   "
myDict = {
    "Company": "Ana Infotech",
    "Name": "Bhavik,{'ITG':0.3,'Pagadhare':'0.6'}",
    "Roll": "Developer",
    "Experience": {'ITG': 0.3, 'Pagadhare': '0.6', 'Ana Infotech': 0.3}
}


# print(myDict['Company'])
# print(myDict['Name'])
# print(myDict["Experience"]['ITG'])
# myDict["Marks"] = [48,32,17,73]
# myDict["Experience"]['Mira'] = 0.3
# myDict["Salary"] = [{'ITG':20, 'pagadhare':0, 'Ana Infotech':5}]
# print(myDict)


"The difference between .get() and [] syntax:"
# print(myDict['Harry'])        # Throws an error if Harry is not present in the dictionary.
# print(myDict.get("Harry"))  # Retrun None but not throw an Error.

'''
Properties of Dictionary:
1)It is Unordered, 2)Mutable, 3)Indexed, 
4)Can't contain duplicate keys(if you add duplicate key, it will override previous key)

Methods:
1)Dictionary.items()                              #-Return list of (Key,Value) tupels
2)Dictionary.keys() /Dictionary.values()         #- Return a list containing dictionary  keys / values
3)Dictionary.update({"Friend":"Dhiru"})
4)Dictionary.get('name')                         #-Return the value of specified keys.
'''

#             ********* Sets in Python ***********
'''
Def: Set is a collection of Unique / non-repetitive elements. It Contain unique values.
S = {1,2,4,5,6,7}
S = set() ---> Empty Set
S.add(1)
S.add(2)

Properties : 1) Unordered, 2) Unindexed, 3) Can't contain duplicate values, 4) There is no way change item in sets.

Methods : 1) len(s), 2) s.remove(), 3) s.pop(), 4) s.clear(), 5) s.union({8,11}), 6) s.intersection({8,11})  ,7) s.add()

'''
#------------------X-------------------------X-------------------------------------X----------------------------------
"""
                                        Zip Function
"""

names=("Dhiru","Bhavik","Janmesh","Abhishek")
company=("MagicBrics","Pagadhare","Canbara","Honda")

# abc=zip(names,company)      #   dict(zip(names,company)) , list(zip(names,company)) ,set(zip(names,company))

# for (a,b) in abc:
#     print(a,":",b)

# eg_dict = dict(zip(names,company))
# print(eg_dict)

eg_list = list(zip(names,company))
print(eg_list)