'''
                                    * Coroutin in Python *
Assume you have created a search function which reads a book and it take 4 seconds time and once it complete reading it
will give answer to any question you ask related to the containt of the book. But initilly it takes the 4 seconds time 
every time you run the code and after that it will take no time at all, this is called Coroutin.

'''

def searcher(): 
    import time
    # Do some 4 second consuming task

    book = "This is a book on Harry and code with harry and good."
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("Text is in the book")
        else:
            print("Text is not in the book")

search = searcher()

print("Search Started")

next(search)
print("Next Method Run")

search.send("Harry")
input("press any key")
search.send("code with")
search.close()

"---------------------X-----------------------X---------------------"
'''
Question. : You have been given 15 letters in text format. You have to write a Coroutin to read all 15 letters and search
for your name in these 15 letters and if your name is in letter then print "Your name is present " else print "Your name 
is not present"
'''

# def name_definer():
#     names = open('text.txt', 'r')
#     reader = names.read()

#     while True:
#         text = (yield)
#         if text in reader:
#             print('Your name is in the list')
#         else:
#             print("You are not in the list")

# inp = input("Enter your name here: ")
# search = name_definer()
# next(search)
# search.send(inp)