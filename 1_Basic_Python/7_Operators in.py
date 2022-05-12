'''
  #1  -    **Short Hand If_Else Notation**

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

print("'A' is greater than 'B'") if a>b else print("'B' is greater than 'A'") # This is called One Liners.

  #2 - Operators in Python:
        i) Arithmetic, 
        
        ii) Assignment: +=, -=, *=, /=, %= 
        
        iii) Logical:   and, or, not 
        
        iv) Comparison: ==, >=, <=, != 
        
        v) Identity:    "is" / "is not"

        vi) Membership: "in" / "not in"
                      Eg.   lst=[17,5,95,10,21,18,16,9] print(324 not in lst) or print(17 in lst)
        vii) Bitwise: & , |

'''



'''                                         Problems                                '''



'Q.1) Write a program to find greatest of 4 numbers entered by the user?'

# num1= int(input('Enter the number1: '))
# num2= int(input('Enter the number2: '))
# num3= int(input('Enter the number3: '))
# num4= int(input('Enter the number4: '))

# if num1>num2:
#     w1=num1
# else: w1=num2

# if num3>num4:
#     w2=num3
# else: w2=num4

# if w1>w2:
#     print(w1, 'is Greatest number')
# else: print(w2, 'is Greatest number')

"____________________OR____________________"


# def grt_num():
#     lst = []
#     for i in range(4):
#        n = int(input("Enter the number: "))
#        lst.append(n)
#     print(lst)
#     m=0
#     for n in lst:
#         if n>m:m=n
#     print(m," is a max number.")

# grt_num()

'''-------------------------------------------------'''


'Q.2) Write a program to find out whether a student is pass or fail, if it requires total 40% and at least 33% in '
'     each subject to pass. Assume 3 subjects and total marks as an input from the user.'

# sub1= int(input('Enter the marks obtained in Mathematics: '))
# sub2= int(input('Enter the marks obtained in Physics:'))
# sub3= int(input('Enter the marks obtained in Chemistry:'))

# if(sub1<33 or sub2<33 or sub3<33):
#     print('You are Fail because you got less than 33 marks in one or more subject.')

# elif(sub1+sub2+sub3)/3 <40:
#     print('You are Fail in Exam due to less than 40%.')

# else:
#     P=(sub1+sub2+sub3)/3
#     print("Congratulations. You have passed the exam. You got",P,'%')

"____________________OR____________________"

# lst = [sub1,sub2,sub3]

# for i in lst:
#     if i<33:
#         print("Student is Failed.")
#         break
# else:
#     if (sub1+sub2+sub3)//3 < 40:
#         print("Student is Failed.")
#     else: print("Student is passed.")

'''-------------------------------------------------'''


'Q.3) A spam comment is defined as text containing following keywords : "Make a lot of money", "Buy now", "Subscribe'
'     this", "Click this". Write a program to detect these spams.'

# text = input('Enter the text : \n')
 
# if("make a lot of money" in text):
#     Spam=True
# elif('buy now' in text):
#     Spam=True
# elif('subscribe this' in text):
#     Spam=True
# elif('click this' in text):
#     Spam=True
# else:
#     Spam=False
# if(Spam):
#     print('This Text is spam')
# else: print('This Text is not spam')

# ---------X------------X------------Metod-2
#Content = input("Enter the text: ")
# lst = ["make a lot of money",'buy now','subscribe this','click this']
# for word in lst:
#     if word in Content:
#         Spam = True
#     else:
#         Spam = False
# if(Spam):
#     print('This Text is spam')
# else: print('This Text is not spam')

'''-------------------------------------------------'''


'Q.4) Write a program to find wether a given string contains less than 10 characters or not.'

# text = input('Enter the text : \n')
# if len(text)>10:
#     print('This text contain maore than 10 characters.')
# else:
#     print('This text contain less than 10 characters.')

'''-------------------------------------------------'''


'Q.5) Write a program to fin out wether a given name is present in a list or not.'
# lst=['ritesh','bhavik','anirudh','atul','nikhil','dhanesh']
# a = input('Enter the name : ')
# if a in lst:
#     print(a, 'is present in the list.')
# else: print(a,'is not in the list') 

'''-------------------------------------------------'''


'Q.6) Write a program to calculate the grade of a student from his marks from the following scheme:'
'     90-100:Ex, 80-89:A, 70-79:B, 60-69:C, 50-59:D, <50:F'

# marks = int(input('Enter your marks :'))
# if marks>=90:
#     grade = 'Ex'
# elif marks>=80:
#     grade = 'A'
# elif marks>=70:
#     grade = 'B'
# elif marks>=60:
#     grade = 'C'
# elif marks>50:
#     grade = 'F'
# print('Your grade is :', grade)

# ---------X------------X------------Metod-2


