import random
import os
from time import sleep

L=('rock','paper','scissors\n')
Win=Loss=Tie=0
options = {1:'rock',2:'paper',3:'scissors',4:'exit'}
winCondition = {'rock':'scissors','paper':'rock','scissors':'paper'}
loseCondition = {'rock':'paper','paper':'scissors','scissors':'rock'}

print("Welcome to Rock Paper Scissors!\n")

while True:
    print(f'''Options
1.{options[1].title()}
2.{options[2].title()}
3.{options[3].title()}
4.{options[4].title()}\n''')
    ch=eval(input("Enter choice number: "))

    if ch not in options:
        print("Invalid choice!\n\
Enter appropriate no for your choice")
    
    elif ch == 4:
        Win=Loss=Tie=0
        print("Exiting game...")
        sleep(1)
        break
        
    else:
        player = options[ch]
        opp=random.sample(L,1)[0]
        sleep(0.5)
        print("You chose ",player.title())
        print("Opponent chose ",opp.title())
        if player==opp:
            Tie+=1
            print("Tie")
        elif winCondition[player] == opp:
            Win+=1
            print("You Win")
        elif loseCondition[player] == opp:
            Loss+=1
            print('You Lose')

        print(f'Wins:{Win}|Loss:{Loss}|Draw:{Tie}')
    sleep(1)
    input("Press 'Enter' key to continue...")
    try:
        os.system('clear')
    except:
        os.system('cls')
    sleep(0.5)