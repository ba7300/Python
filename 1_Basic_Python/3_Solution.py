"Q.1 Write a program to display a user entered name followed by Good Afternoon using input() function ?"
# name = input("Enter a name: ")
# print("Good Evening", name)


''' Q.2 Write a program to fill in a letter template given below with the name and date ?
                Letter = "Dear |<Name>|,
                          You are selected !
                          |<Date>|"
'''
                          
                          # Use "replace" function.
# letter = ''' 
# Dear <|Name|>,
# Greeeting from abcd coding house. I am happy to tell you about your selection.
# You are selected! Have a great day ahead!
# Thanks and Regards,
# Bill
# <|Date|>
# '''
# name = input("Enter the name: ")
# date = input("Enter the date: ")
# letter = letter.replace("<|Name|>",name)
# letter = letter.replace("<|Date|>",date)
# print(letter)


"Q.3 Write a program to detect double space in a string ?"
# paragraph = "This is a double space  statement  problrm which we are going to solve here."
# f = paragraph.find("  ")
# print(f)


"Q.4 Replace the double space from above problem with single space ?"
# paragraph = "We are going to replace double space  to  single spaece in this problem"
# f = paragraph.replace("  ",' ')
# print(f)