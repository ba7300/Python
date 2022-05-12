'''
                        *** Guess The Number ***
'''

N = 17
print("Total number of guesses are 9")
User_Guess = None
Remaining_Guesses = 9
Number_of_Guess = 0
while(Remaining_Guesses != 0):
    User_Guess = int(input("Enter the number: "))
    Remaining_Guesses -=1
    Number_of_Guess +=1

    if User_Guess == N:  
        print("Congrats, You guessed the right number.")
        print(f"You took {Number_of_Guess} guesses to complete the task.")
        break
    else:
        if User_Guess > N:
            print(f"You guessed it wrong! Enter a smaller number. Remaining guesses are {Remaining_Guesses} only.")
        else:
            print(f"You guessed it wrong! Enter a larger number. Remaining guesses are {Remaining_Guesses} only.")
            
else:
    print("Game Over ! You are out of guesses.")


'X______________________X_________________________X____________________________X_____________________________X'
'''
                                Using For Loop
'''

N = 17
R = 10
print('You have 9 Guesses only !')
for i in range(1,R):
    U = int(input("Enter the number: "))
    if U==N:
        print(f"Congratulations !!! You Guessed the right number. You did this in {i} guesses.")
        break
    else:      
        if U > N:
            print(f"You have entered larger number. please enter smaller one.Only {R-1-i} guesses remain.")
        else:
            print(f"You have entered smaller number. please enter larger one.Only {R-1-i} guesses remain.")
else:
    print("Game Over!!! You  are out of guesses. Better luck next time.. ")



