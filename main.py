import random
import time

# Get dice roll
def roll():
    min_value = 1
    max_value = 50
    return random.randint(min_value, max_value)

# Game function
def main():
    print("Welcome to my PIG game, first to 50 points wins!\n")

    while True:
        # Get number of players
        while True:
            players = input("Enter the number of players (2-4): ")
            if players.isdigit():
                players = int(players)
                if 2 <= players <= 4:
                    break
                else:
                    print("Players must be between 2 - 4.")
            else:
                print("Please enter a valid number (2-4).\n")

        # Max score and create score list depending on player count
        MAX_SCORE = 50
        player_scores = [0 for _ in range(players)]

        # Game loop
        while True:
            # Go through each player's turn
            for player_index in range(players):
                print(f"\nPlayer {player_index + 1}'s turn has just started! Your score is: {player_scores[player_index]}\n")
                current_score = 0
                while True:
                    should_roll = input("Would you like to roll (y)? ").lower()
                    if should_roll != "y":
                        print(f"Player {player_index + 1} ends their turn with {current_score} this round!")
                        break

                    value = roll()
                    if value == 1:
                        print("You rolled a 1! Turn over, no points earned.")
                        current_score = 0
                        break
                    else:
                        print(f"You rolled a: {value}")
                        current_score += value
                        print(f"Your current round score is: {current_score}")

                player_scores[player_index] += current_score
                print(f"Player {player_index + 1}'s total score is: {player_scores[player_index]}")
                
                # Sleep for a more friendly UX
                time.sleep(1)

            # Check if any player has reached 50 points
            if max(player_scores) >= MAX_SCORE:
                break

        # Determine winner
        winner_index = player_scores.index(max(player_scores))
        print(f"\nCongratulations! The winner is Player {winner_index + 1} with {player_scores[winner_index]} points!")

        # Replay option
        replay = input("Do you want to play again (y)? ").lower()
        if replay != "y":
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
