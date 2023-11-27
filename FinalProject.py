import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * (4 * len(row) - 1))

def is_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(4):
        if all(board[row][col] == player for row in range(4)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(4)):
        return True
    if all(board[i][3 - i] == player for i in range(4)):
        return True

    return False

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def get_computer_move(board):
    # Check if any move can make the computer win
    for row in range(4):
        for col in range(4):
            if board[row][col] == " ":
                board[row][col] = "O"
                if is_winner(board, "O"):
                    return row, col
                board[row][col] = " "

    # Check if any move can block the player from winning
    for row in range(4):
        for col in range(4):
            if board[row][col] == " ":
                board[row][col] = "X"
                if is_winner(board, "X"):
                    return row, col
                board[row][col] = " "

    # Choose a random move
    available_moves = []
    for row in range(4):
        for col in range(4):
            if board[row][col] == " ":
                available_moves.append((row, col))

    return random.choice(available_moves)

def play_tic_tac_toe():
    board = [[" " for _ in range(4)] for _ in range(4)]
    current_player = "X"

    while True:
        print_board(board)

        if current_player == "X":
            row = int(input("Enter the row (0-3): "))
            col = int(input("Enter the column (0-3): "))
            if board[row][col] == " ":
                board[row][col] = current_player
                if is_winner(board, current_player):
                    print("Congratulations! You win!")
                    break
                elif is_board_full(board):
                    print("It's a tie!")
                    break
                current_player = "O"
            else:
                print("Invalid move. Try again.")
        else:
            
            row, col = get_computer_move(board)
            board[row][col] = current_player
            if is_winner(board, current_player):
                print("Computer wins!")
                break
            elif is_board_full(board):
                print("It's a tie!")
                break
            current_player = "X"

play_tic_tac_toe()
