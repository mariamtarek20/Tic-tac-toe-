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

# Function to make a player move
def player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move >= 0 and move < 9 and board[move] == " ":
                return move
            else:
                print("Invalid move. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number (1-9).")

# Depth-First Search (DFS) AI algorithm
def dfs_ai(board, player):
    for i in range(9):
        if board[i] == " ":
            board[i] = player
            if check_win(board, player):
                return i
            board[i] = " "

    for i in range(9):
        if board[i] == " ":
            board[i] = "O" if player == "X" else "X"
            if check_win(board, "O" if player == "X" else "X"):
                return i
            board[i] = " "

    while True:
        move = random.randint(0, 8)
        if board[move] == " ":
            return move

# Main game loop
def play_game():
    player = "X"
    while True:
        display_board(board)
        
        if player == "X":
            move = player_move()
        else:
            move = dfs_ai(board, player)
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


