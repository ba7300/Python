

'''
Q1.    Write a program to read a text from a given file 'poem.txt' and find out wether it contains the word 'twinkle'. 
'''
# with open('poem.txt') as f:
#     r = f.read()
#     print(r)
# if 'twinkle' in r.lower():
#     print('Twinkle is present in the file.')
# else: print('Twinkle is not present in the file.')


'''
Q2.    The game() function in a program, let's a user play a game and returns the score as an integer. You need to read a
       file 'Hiscore.txt' which is either blank or contains previous hi-score. You need to write a program to update the 
       Hi-score whenever game() braks the Hi-score.
'''
# Q.2) Solution :

def game(a):
    return a

# Calling game function:   
score = game(67)

# program for Read-Write Operation :

with open('Highscore.txt') as f:
    rf = f.read()

if rf == '':
    with open('Highscore.txt','w') as f:
        f.write(str(score))

elif int(rf) < score:
    with open('Highscore.txt','w') as f:
        f.write(str(score))


'''
Q3.    Write a progam to generate multiplication table from 2 to 20 and write it to the different files. Place these 
       files in a folder.
'''
# Q.3) Solution :

for i in range(2,21):
    with open(f"Multiplication_Table/ Table of {i}'s.txt",'w') as f:
    
        for j in range(1,11):
            f.write(f"{i}X{j} = {i*j}")
            if j != 10:
                f.write("\n")


'''
Q4.    A file contain a word "Donkey" multiple times. You need to write a program which replace this word with
       ###### by updating the same file.
'''
# Q.4) Solution :

# with open('sample.txt') as f:
#     r = f.read()

# r = r.replace('Donkey','######')
# with open('sample.txt','w') as f:
#     f.write(r)


'''
Q5.    Repeat (Q-4) for a list of such words to be censored.
'''
# Q.5) Solution :

# from os import replace

# words = ['Donkey','Monkey','shit','Dumb']

# with open('sample1.txt') as f:
#     rf = f.read()

# for word in words:
#     rf = rf.replace(word,'******')
#     with open('sample1.txt','w') as f:
#         f.write(rf)


'''
Q6.    Write a program to mine a log file  and find out wether it contains "Python".
'''
# Q.6) Solution :

# with open('log.txt') as f:
#     content = f.read()

# if "python" in content.lower():
#     print('Python is present in the Log File.')
# else:
#   print('Python is not present in the Log File.')


'''
Q7.    Write a progam to find out the line number where python is present from (Q-6).
'''
# Q.7) Solution :

# content = True
# i = 1

# with open('log.txt') as f:

#     while content:
#         content = f.readline()

#         if 'python' in content.lower():
#             print(content)
#             print(f"Yes ! Python is present on line number {i}")
#             print()     
#         i += 1


'''
Q8.    Write a program to make a copy of a text file "this.txt".
'''
# Q.8) Solution :

# with open('this.txt') as f:
#     cont = f.read()
# with open("copy.txt",'w') as f:
#     f.write(cont)


'''
Q9.    Write a program to find out whethe a file is identical or matches the content of another file.
'''
# Q.9) Solution :

# file1 = "this.txt"
# file2 = "copy.txt"
# with open(file1) as f:
#     f1 = f.read()
# with open(file2) as f:
#     f2 = f.read()
# if f1 == f2 :
#     print ("Files are identical")
# else: 
#     print ("Files are not identical")


'''
Q10.   Write a program to wipe out the content of a file using python.
'''
# Q.10) Solution :

# filename = 'copy.txt'
# with open(filename,'w') as f:
#     f.write('')


'''
Q11.   Write a program to rename a file to "renamed_by_python.txt".
'''
# Q.11) Solution :

# import os

# o_name = 'score_rank.txt'
# n_name = 'Highscore.txt'

# with open(o_name) as f:
#     dr = f.read()
# with open(n_name,'w')as f:
#     f.write(dr)

# os.remove(o_name)