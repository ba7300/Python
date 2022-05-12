''' 
                                 " Python file handling "  

1. "r" : Open file for reading
2. "w" : Open a file for writing
3. "x" : Creates file if not exist
4. "a" : Append or Add more content to a file
5. "t" : text mode, if I want to open my file in text 
6. "b" : Binary mode
7. "+" : Read & Write

'''

# with open('Chap_9_Que.txt','w') as f:

    

"Read a File"
# f = open('sampletext.txt','r')          # Open the file in read mode
# tr = f.read()                           # Read its content
# tr = f.read(5)                         # Read 1st five chracters from the file
# tr = f.readline                         # Read one line from the file
# print(tr)                               # Print its content
# f.close()                               # Close the file

"Write a File"
# f = open('writefile.txt','w')
# f.write('I am currently living in Panvel..wold you like to come')
# f.close()


"Append a File"
# f = open('sampletext.txt','a')
# f.write("Write whatever you want ...")
# f.close()


'''                  #   WITH Statement       #                  
'''

"Read using WITH Statement"
# with open('another.txt') as f:
#     a = f.read()
#     print(a)

"Write using WITH Statement"
# with open('another.txt','w') as f:
#     f.write('I will show you M**F**')


"Perform read and write both operations"
# f = open('sample1.txt', 'r+')
# f.write('Hi, I am back!')
# f.close

'''
    "tell()" function will give Position of file pointer.
    "seek()" function will give desired pointer value.  

'''

# with open('sample1.txt')as f:
#     print(f.tell())
#     f.readline()
#     print(f.tell())

#     f.seek(3)
#     print(f.readline())

