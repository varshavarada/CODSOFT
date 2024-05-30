import random
def rock_paper_scissors():
    ans = ("rock", "paper", "scissors")
    computer_choice = random.choice(ans)
    return computer_choice
opt = "Y"
while opt.upper() == "Y":
    player_score = 0
    comp_score = 0
    try:
        num_r = int(input("How many rounds will you be playing?: ")) 
        for i in range(num_r):
            g = input("Select rock, paper, or scissors: ").lower()
            comp = rock_paper_scissors()            
            if g == "rock":
                if comp == "scissors":
                    player_score += 1
                    print("You won +1 point")
                elif comp == "paper":
                    comp_score += 1
                    print("Comp won +1 point")
                else:
                    print("Draw")              
            elif g == "paper":
                if comp == "scissors":
                    comp_score += 1
                    print("Comp won +1 point")
                elif comp == "rock":
                    player_score += 1
                    print("You won +1 point")
                else:
                    print("Draw")              
            elif g == "scissors":
                if comp == "rock":
                    comp_score += 1
                    print("Comp won +1 point")
                elif comp == "paper":
                    player_score += 1
                    print("You won +1 point")
                else:
                    print("Draw")
            else:
                print("Invalid choice, round forfeited.")            
            print("The computer chose:", comp)        
        print(f"The Computer has a score of {comp_score} and You have a score of {player_score}")   
        if comp_score > player_score:
            print("The Computer won")
        else:
            print("You won")        
    except ValueError:
        print("Invalid input. Please enter a number.")  
    opt = input("Do you wish to try again? Y/N: ").upper()
