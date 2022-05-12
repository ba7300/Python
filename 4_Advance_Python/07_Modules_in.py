'''
X__________X______________X__________* OS Module in Python *_________X_______________X______________X
'''

from copyreg import pickle
import os
# print(dir(os))                               -----> It will print all diectories of os on which you can work.

# print(os.getcwd())                           -----> It will give you current working directory CWD.

# os.chdir("C://")                             -------> It will change CWD.
# print(os.getcwd())

# print(os.listdir("C://"))                    -----> It will give you list of all files present in the C drive.

# os.mkdir('This')                             ----> It will create "This" folder in current project
# os.makedirs('The/one')

# os.rename("harry.txt","codewithharry.txt")                    ----> It will rename the file.

# print(os.environ.get('Path'))
# print(os.path.join("C://","/harry.txt"))

# print(os.path.exists("C://Program Files2"))                   ----> Give True or False Value if the path exist.
# print(os.path.isfile("C://Program Files"))                    ----> Give True or False Value if the file exist.


'''
X__________X______________X__________* JSON Module in Python *_________X_______________X______________X


- JSON stand for Java Script Object Notation. 
- It's way of sending data, kind of web protocol type and you can call the data or send the data using JSON and you can
  parse your data in broweser very easily.

- JSON is a syntax for storing and exchanging data.
- Python has a built-in package called json, which can be used to work with JSON data.
________________________________________________________________________________________________________________________
* Parse JSON :- 
  Convert from JSON to Python :   If you have a JSON string, you can parse it by using the "json.loads()" method.
                                                
* Convert from Python to JSON : If you have a Python object, you can convert it into a JSON string by using the 
                                "json.dumps()" method.
________________________________________________________________________________________________________________________

-json.loads()--------->  It is used to convert a json string to an dictonary

 json.dump()--------->   It is used to convert a dictonary to an json compatible string.

 json.load()---------->  It is used to read a file which contains an json object {but "json.load" takes file object 
                         which  consists of 'keys' and 'value' pairs saperated by ":" and returns a json object.}

- "sort_keys" parameter data ke "key:value" pairs ko sort krne ke kam ata hai.
'''

import json

# data1 = '{"var1":"harry", "var2":73}'
# # print(data['var1'])           # It will throw an error

# parsed = json.loads(data1)       #      json.loads()--------->  It is used to convert a json string to an dictonary
# print(parsed)                   #       to get the data in "key:value" form, we Parse the JSON
# print('\n')
# print(parsed['var1'])


# data2 = {
#     "Channel_name" : "CodeWithHarry",
#     "Cars" : ['Jaguar', 'LandRower', 'BMW', 'TATA'],
#     "Fridge" : ('Roti', 540),
#     "Is_Bad": False
# }

# jscomp = json.dumps(data2)     #json.dumps()---------> It is used to convert a dictonary to an json compatible string.
# print(jscomp)



'''
X__________X______________X__________* Pickle Module in Python *_________X_______________X______________X

- Python pickle module is used for serializing and de-serializing a Python object structure. 

* Defination:
             The process to converts any kind of python objects (list, dict, etc) into byte streams (0s and 1s) is 
   called "pickling" or "serialization" or "flattening" or "marshalling".
   We can converts the byte stream  (generated through pickling) back into python objects by a process 
   called as "unpickling".

- Any object in Python can be pickled so that it can be saved on disk. 
- What pickle does is that it “serializes” the object first before writing it to file. 
- Pickling is a way to convert a python object (list, dict, etc.) into a character stream. 


*Note : 
        pickle.load() - takes file object and return corresponding python format (readable ) 
        pickle.loads() - takes the binary format and returns python format
        pickle.dumps() - takes the variable and returns binary string

'''
# import pickle

# cars = ["TATA", "JAGUAR", "BMW", "LEMBORGHENI"]

# file = "mycar.pkl"
# fileobj = open(file, 'wb')
# pickle.dump(cars, fileobj)
# fileobj.close()


# file = "mycar.pkl"
# fileobj = open(file, 'rb')
# mycar = pickle.load(fileobj)
# print(mycar)

"X____________X__________________X______________Swati Chawla Code____________X________________X_________________X"

import pickle

def write():
  f = open("BinaryWrite.dat","wb")
  frnds = ["Bhavik",'Dhiru',"Viy",'Shubham',"Janmesh","Abhi","Sandeep","Viraj"]
  pickle.dump(frnds, f)
  f.close()

def read():
  f = open("BinaryWrite.dat",'rb')
  myfrnds = pickle.load(f)
  print(myfrnds)
  f.close()

write()
print("Data written in file successfully...")
read()