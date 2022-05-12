
"""                                  Snake Water Game                                            
"""

import random

lst = ['s','w','g']

chance = 10
no_of_chance = 0
Comp_points = 0
Your_points = 0

# print("s for snake \nw for water \ng for gun \n ")

while no_of_chance < 10:
    U_input = input("\n Enter (s) for Snake, (w) for Water, (g) for Gun:")
    Comp_input = random.choice(lst)

    if U_input.lower() == Comp_input:
        print("Tie, both 0 poits to each.")
    
    # If User Enter Snake
    elif U_input.lower()  == 's' and Comp_input == 'g':
        Comp_points += 1
        print(f"Your guess is {U_input} and Computer guess is {Comp_input}.")
        print("Computer wins 1 point. \n") 
        print(f"Computer point is {Comp_points} and Your point is {Your_points} \n")

    elif U_input.lower()  == 's' and Comp_input == 'w':
        Your_points += 1
        print(f"Your guess is {U_input} and Computer guess is {Comp_input}.")
        print("You win 1 point. \n") 
        print(f"Computer point is {Comp_points} and Your point is {Your_points} \n")


    # If User Enter Water
    elif U_input.lower()  == 'w' and Comp_input == 's':
        Comp_points += 1
        print(f"Your guess is {U_input} and Computer guess is {Comp_input}.")
        print("Computer wins 1 point. \n") 
        print(f"Computer point is {Comp_points} and Your point is {Your_points} \n")

    elif U_input.lower()  == 'w' and Comp_input == 'g':
        Your_points += 1
        print(f"Your guess is {U_input} and Computer guess is {Comp_input}.")
        print("You win 1 point. \n") 
        print(f"Computer point is {Comp_points} and Your point is {Your_points} \n")


    # If User Enter Gun
    elif U_input.lower()  == 'g' and Comp_input == 'w':
        Comp_points += 1
        print(f"Your guess is {U_input} and Computer guess is {Comp_input}.")
        print("Computer wins 1 point. \n") 
        print(f"Computer point is {Comp_points} and Your point is {Your_points} \n")

    elif U_input.lower()  == 'g' and Comp_input == 's':
        Your_points += 1
        print(f"Your guess is {U_input} and Computer guess is {Comp_input}.")
        print("You win 1 point. \n") 
        print(f"Computer point is {Comp_points} and Your point is {Your_points} \n")

    
    else:
        print( "You have entered wrong input !")
    
    no_of_chance += 1
    print(f"{chance - no_of_chance} is left out of {chance} \n")


print(" GAME is OVER !!!")


if Comp_points > Your_points:
    print(f"Computer score is {Comp_points} and Your score is {Your_points}.")
    print("Computer Won the Game.")

elif Comp_points < Your_points:
    print(f"Computer score is {Comp_points} and Your score is {Your_points}.")
    print("You Won the Game.")

else:
    print(f"Computer score is {Comp_points} and Your score is {Your_points}.")
    print('The Game is Draw')