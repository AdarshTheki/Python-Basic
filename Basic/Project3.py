# Create Project Rock, Papper, Scissors Using Random Modules.

import random
l = ['Rock','Papper','Scissor']

while True:
    countuser=0
    countcomp=0
    uc = int(input('''
    Game Start......
    1   Yes
    2   No | Exit 
    '''))

    if uc==1:
        for a in range(1,6):
            userInput = int(input('''
    1   Rock
    2   Papper
    3   Scissor
            '''))
            if userInput==1:
                uchoice = 'Rock'
            elif userInput==2:
                uchoice = 'Papper'
            elif userInput==3:
                uchoice = 'Scissor'
            Cchoice=random.choice(l)

            if Cchoice==uchoice:
                print("Computer Value:",Cchoice)
                print("User Value:",uchoice)
                print("Game Drow...")
                countuser = countuser+1
                countcomp = countcomp+1
            elif (uchoice=='Rock' and Cchoice=='Scissor') or (uchoice=='Papper' and Cchoice=='Rock') or (uchoice=='Scissor' and Cchoice=='Papper'):
                print("Computer Value:",Cchoice)
                print("User Value:",uchoice)
                print("You Win....")
                countuser = countuser+1
            else:
                print("Computer Value:",Cchoice)
                print("User Value:",uchoice)
                print("Computer Win....")
                countcomp = countcomp+1
        if countuser==countcomp:
            print("Final Game Drow...")
            print("User Score:",countuser)
            print("Computer Score:",countcomp)
        elif countuser > countcomp:
            print("\n\tFinal Game You win...")
            print("User Score:",countuser)
            print("Computer Score:",countcomp)
        else:
            print("\n\tFinal Game Computer Win...")
            print("User Score:",countuser)
            print("Computer Score:",countcomp)
    break