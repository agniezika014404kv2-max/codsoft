# Rock-Paper-Scissors Game
# Codsoft Internship - Python Programming

import random

def play_game():
    print("🎮 Welcome to Rock-Paper-Scissors!")
    print("Instructions: Type 'rock', 'paper', or 'scissors' to play.")

    # Score tracking
    user_score = 0
    computer_score = 0

    while True:
        # User input
        user_choice = input("\nEnter your choice (rock/paper/scissors): ").lower()

        # Validate input
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Please try again.")
            continue

        # Computer choice
        computer_choice = random.choice(["rock", "paper", "scissors"])
        print(f"🧑 You chose: {user_choice}")
        print(f"💻 Computer chose: {computer_choice}")

        # Game logic
        if user_choice == computer_choice:
            print("🤝 It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("🎉 You win this round!")
            user_score += 1
        else:
            print("😢 Computer wins this round!")
            computer_score += 1

        # Display scores
        print(f"📊 Scores → You: {user_score} | Computer: {computer_score}")

        # Play again option
        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            print("\n🏁 Final Scores:")
            print(f"🧑 You: {user_score}")
            print(f"💻 Computer: {computer_score}")
            print("Thanks for playing! Goodbye 👋")
            break

# Run the game
play_game()
