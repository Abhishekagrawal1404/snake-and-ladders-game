import random

# Define the board for the game
board = {
    3: 17,
    7: 11,
    20: 29,
    19: 5,
    30: 1,
    27: 13
}

# Define the game function
def play_game():
    player_position = 0
    while True:
        # Roll the dice
        input("Press Enter to roll the dice...")
        roll = random.randint(1, 6)
        print("You rolled a", roll)
        
        # Move the player on the board
        player_position += roll
        if player_position > 30:
            player_position = 30
            
        # Check if the player landed on a snake or ladder
        if player_position in board:
            new_position = board[player_position]
            if new_position > player_position:
                print("You climbed a ladder!")
            else:
                print("You got swallowed by a snake!")
            player_position = new_position
        
        # Check if the player won the game
        if player_position == 30:
            print("Congratulations! You won!")
            break
        
        # Print the player's current position
        print("You are now at position", player_position)

# Play the game
play_game()
