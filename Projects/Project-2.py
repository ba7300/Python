'''
We are going to write a program that generates  a random number and asks the user to guess it.
If the player's guess is higher than the actual number, the program displays "Lower number please!".
Similarly if the user's guess is too low, the program prints "Higher number please!".
When the user guesses the correct number, the program displays the number of guesses the palyer used 
to choose correct number.

'''
import random 
randNmb = random.randint(1,100)
guess = 0
UserGuess = None

while(UserGuess != randNmb):
    UserGuess = int(input("Guess the number: "))
    guess +=1
    
    if UserGuess == randNmb:
        print("You guessed it right !")
        
    else:
        if UserGuess > randNmb:
            print("You guessed it wrong! Enter a smaller number.")
        else:
            print("You guessed it wrong! Enter a larger number.")

print(f"You guessed the number in {guess} guesses.")
