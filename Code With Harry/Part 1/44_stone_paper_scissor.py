import random
i = 0
c = 0
p = 0

while (i<1):
    computer = random.randint(1,3)
    if computer == 1:
        comp = "Stone"
    elif computer == 2:
        comp = "Paper"
    else:
        comp = "Scissor"

    player = str(input("Enter your choice\n(Stone/Paper/Scissor): "))
    if (comp == "Stone" and player == "Scissor"):
        print("Computer Wins")
        c+=1
    elif (comp == "Paper" and player == "Stone"):
        print("Computer Wins")
        c+=1
    elif (comp == "Scissor" and player == "Paper"):
        print("Computer Wins")
        c+=1
    elif (player == "Scissor" and comp == "Paper"):
        print("Player Wins")
        p+=1
    elif (player == "Stone" and comp == "Scissor"):
        print("Player Wins")
        p+=1
    elif (player == "Paper" and comp == "Stone"):
        print("Player Wins")
        p+=1
    else:
        print("Tie!!")
    a = str(input("Do you want to continue to next round\n(y/n) "))
    if (a == "n"):
        i+=1
    
print(f'''Game has ended!!
Computer has won {c} rounds
Player has won {p} rounds''')

