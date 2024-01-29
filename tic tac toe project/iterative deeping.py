import random

# Initialize the Tic Tac Toe board
board = [" " for _ in range(9)]

# Function to display the Tic Tac Toe board
def display_board(board):
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i + 1]} | {board[i + 2]}")
        if i < 6:
            print("---------")

# Function to check for a win
def check_win(board, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# Function to check for a tie
def check_tie(board):
    return " " not in board


# Iterative Deepening AI algorithm
def iterative_deepening_ai(board, player, max_depth):
    # Get a list of available moves (empty cells) on the board
    available_moves = [i for i, cell in enumerate(board) if cell == " "]
    
    # Initialize the best move to None
    best_move = None

    # Iterate over depths from 1 to max_depth
    for depth in range(1, max_depth + 1):
        # Iterate over available moves
        for move in available_moves:
            # Make a move on a copy of the board
            board[move] = player
            
            # Check if the current move leads to a win or if the maximum depth is reached
            if check_win(board, player) or depth == max_depth:
                # Return the current move if it meets the conditions
                return move
            
            # Undo the move (backtrack) for further exploration
            board[move] = " "

    # If no winning move is found, return a random move among the available moves
    return random.choice(available_moves) if available_moves else None


# Main game loop
def play_game():
    player = "X"
    max_depth = 9  # Maximum depth to search (all cells)

    while True:
        display_board(board)
        
        if player == "X":
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move >= 9 or board[move] != " ":
                print("Invalid move. Please try again.")
                continue
        else:
            move = iterative_deepening_ai(board, player, max_depth)
            if move is None:
                print("It's a tie!")
                break
            print(f"Computer player chose position {move + 1}")

        board[move] = player

        if check_win(board, player):
            display_board(board)
            print(f"{player} wins!")
            break
        elif check_tie(board):
            display_board(board)
            print("It's a tie!")
            break

        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    play_game()


