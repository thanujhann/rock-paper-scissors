
import random
import string

#hand = input("Enter your hand: ").lower()


comp_hands = ["rock", "scissors", "paper"]

#choice = random.choice(comp_hands)
player_score = 0
comp_score = 0

while True:

    hand = input("Enter your hand: ").lower()

    choice = random.choice(comp_hands)

    

    if hand == "rock" or hand == "scissors" or hand == "paper":
        print("Computer: " + choice)

        
        if choice == "rock" and hand == "paper":
            print("Paper beats Rock! You Win!")
            player_score += 1
        elif choice == "rock" and hand == "rock":
            print("Rock + Rock = Draw ")
            
        elif choice == "rock" and hand == "scissors":
            print("Rock beats scissors! You Lose!")
            comp_score += 1
        elif choice == "paper" and hand == "rock":
            print("Paper beats Rock! You Lose")
            comp_score += 1
        elif choice == "paper" and hand == "paper":
            print("Paper + Paper = Draw rude boi")
            
        elif choice == "paper" and hand == "scissors":
            print("Scissors beats Paper! You Win!")
            player_score += 1
        elif choice == "scissors" and hand == "rock":
            print("Rock beats Scissors! You Win")
            player_score += 1
        elif choice == "scissors" and hand == "paper":
            print("Scissors beats Paper! You Lose")
            comp_score += 1
        elif choice == "scissors" and hand == "scissors":
            print("Scissors + Scissors = DRAW BIG MAN!")
    
    elif hand == "end":
        print("Your score: ",  player_score)
        print("Computer score: ", comp_score)
        break

    else:
        print("THAT AINT NO HAND BIG G")
