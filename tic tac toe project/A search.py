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

# A* AI algorithm (simplified)
def a_star_ai(board, player):
    available_moves = [i for i, cell in enumerate(board) if cell == " "]
    
    # Simple heuristic: The AI tries to win if possible, else it blocks the opponent.
    for move in available_moves:
        board[move] = player
        if check_win(board, player):
            return move
        board[move] = " "
    
    for move in available_moves:
        board[move] = "X" if player == "O" else "O"
        if check_win(board, "X" if player == "O" else "O"):
            return move
        board[move] = " "
    
    return random.choice(available_moves) if available_moves else None

# Main game loop
def play_game():
    player = "X"
    while True:
        display_board(board)
        
        if player == "X":
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move >= 9 or board[move] != " ":
                print("Invalid move. Please try again.")
                continue
        else:
            move = a_star_ai(board, player)
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

