import random
from queue import PriorityQueue

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

# Uniform Cost Search (UCS) AI algorithm to explore possible moves
def ucs_ai(board, player):
    def calculate_cost(board):
        # In this simple implementation, the cost is the number of empty cells on the board.
        return board.count(" ")

    priority_queue = PriorityQueue()
    priority_queue.put((0, board))

    while not priority_queue.empty():
        cost, current_board = priority_queue.get()

        if check_win(current_board, player):
            return current_board.index(player)

        empty_cells = [i for i, cell in enumerate(current_board) if cell == " "]
        for cell in empty_cells:
            new_board = current_board.copy()
            new_board[cell] = player
            new_cost = calculate_cost(new_board)
            priority_queue.put((new_cost, new_board))

    # If no immediate win is found, make a random move
    empty_cells = [i for i, cell in enumerate(board) if cell == " "]
    return random.choice(empty_cells)

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
            move = ucs_ai(board, player)
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



