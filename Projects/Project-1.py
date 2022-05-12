'''   snake_water_gun Game   '''

import random

def GameWin(comp,you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True

    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

print("Computer's Turn: Snake(s) Water(w) & Gun(g) :")
Comp_Choise = random.randint(1,3)
if Comp_Choise == 1:
 comp = 's'
elif Comp_Choise == 2:
 comp = 'w'
elif Comp_Choise == 3:
 comp = 'g'
 
you = input('Your Turn:Snake(s) Water(w) & Gun(g) ?: ')

a = GameWin(comp,you)

print(f"Computer chose : {comp}")
print(f"You chose : {you}")


if a == None:
    print("This game is a tie !")
elif a:
    print("You Won !")
else:
    print('You Lost !')
