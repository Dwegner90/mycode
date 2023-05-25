import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == 'rock' and computer_choice == 'scissors') or
        (player_choice == 'paper' and computer_choice == 'rock') or
        (player_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    choices = ['rock', 'paper', 'scissors']

    while True:
        player_choice = input("Enter your choice (rock/paper/scissors): ")
        player_choice = player_choice.lower()

        if player_choice not in choices:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(choices)

        print(f"You chose {player_choice}.")
        print(f"The computer chose {computer_choice}.")

        result = determine_winner(player_choice, computer_choice)
        print(result)

        play_again = input("Do you want to play again? (yes/no): ")
        play_again = play_again.lower()

        if play_again != 'yes':
            break

    print("Thank you for playing!")

# Start the game
play_game()

