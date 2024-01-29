from collections import deque
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

# Breadth-First Search (BFS) AI algorithm
def bfs_ai(board, player):
    queue = deque()
    for i in range(9):
        if board[i] == " ":
            temp_board = board.copy()
            temp_board[i] = player
            queue.append(temp_board)

    while queue:
        current_board = queue.popleft()
        if check_win(current_board, player):
            return current_board.index(player)

    return random.choice([i for i, cell in enumerate(board) if cell == " "])

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
            move = bfs_ai(board, player)
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


