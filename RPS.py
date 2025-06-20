import random

choose = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0

print("Welcome to Rock, Paper, Scissors!")
print("Type 'q' anytime to quit.\n")

while True:
    user = input("Enter a choice (rock, paper, scissors) or type 'q' to quit: ").lower()

    if user == 'q':
        print("\nThanks for playing!")
        print(f"\nYour Score: {user_score}")
        print(f"Computer's Score: {computer_score}")
        
        if user_score > computer_score:
            print(f"You won the game with {user_score - computer_score} point(s) more than the computer! 🎉")
        elif user_score < computer_score:
            print(f"You lost the game with {computer_score - user_score} point(s) less than the computer. 😞")
        else:
            print("It's a tie overall!")
        break

    if user not in choose:
        print("Invalid input. Please enter 'rock', 'paper', or 'scissors'.\n")
        continue

    computer = random.choice(choose)
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")

    if user == computer:
        print("It's a tie!\n")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win this round!\n")
        user_score += 1
    else:
        print("Computer wins this round!\n")
        computer_score += 1
