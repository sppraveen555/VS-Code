import random


def show_board(board):
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


def check_winner(board, symbol):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for pos in win_positions:
        if board[pos[0]] == symbol and board[pos[1]] == symbol and board[pos[2]] == symbol:
            return True

    return False


def board_full(board):
    for item in board:
        if item not in ["X", "O"]:
            return False
    return True


def player_move(board, symbol):
    move = int(input("Choose a position (1-9): ")) - 1

    if board[move] not in ["X", "O"]:
        board[move] = symbol
    else:
        print("Position already taken!")
        player_move(board, symbol)


def ai_move(board, symbol):
    empty = []

    for i in range(9):
        if board[i] not in ["X", "O"]:
            empty.append(i)

    move = random.choice(empty)
    board[move] = symbol


def tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!")

    name = input("Enter your name: ")

    if name == "":
        name = "Player"

    board = ["1","2","3","4","5","6","7","8","9"]

    player_symbol = input("Choose X or O: ").upper()

    if player_symbol == "X":
        ai_symbol = "O"
    else:
        ai_symbol = "X"

    turn = "Player"

    while True:
        show_board(board)

        # Player turn
        if turn == "Player":
            player_move(board, player_symbol)

            if check_winner(board, player_symbol):
                show_board(board)
                print(name, "wins!")
                break

            turn = "AI"

        
        else:
            ai_move(board, ai_symbol)

            if check_winner(board, ai_symbol):
                show_board(board)
                print("AI wins!")
                break

            turn = "Player"

        
        if board_full(board):
            show_board(board)
            print("It's a tie!")
            break

tic_tac_toe()