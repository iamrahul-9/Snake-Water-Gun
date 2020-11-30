import random as rd

def game_win(Comp,You):
    if Comp == You:
        return None   
    elif Comp == 's':
        if You == 'w':
            return False
        elif You == 'g':
            return True
    elif Comp == 'w':
        if You == 'g':
            return False
        elif You == 's':
            return True
    elif Comp == 'g':
        if You == 's':
            return False
        elif You == 'w':
            return True        
print("******** The Snake, Water, Gun Game ********")
print("         ==========================         ")
print("Computer Turn: Snake(s), Water(w) or Gun(g)?")
randNO = rd.randint(1, 3)
if randNO == 1:
    Comp = 's'
elif randNO == 2:
    Comp = 'w'
else:
    Comp = 'g'
You = input("Your Turn: Snake(s), Water(w) or Gun(g)?: ")
a = game_win(Comp,You)

print(f"Computer chose {Comp}")
print(f"Your chose {You}")

if a == None:
    print("The game tie!")
elif a:
    print("Congrats! You Win")
else:
    print("You Lose! Better luck next time")

