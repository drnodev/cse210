'''
Tic-Tac-Toe
Author: Nelson Ortega
'''


def main():
    board = [*range(1, 10)]
    print("Wellcome to tic tac toe")
    print("X start")
    print_board(board)
    play(board)


def print_board(board):
    print()
    # first line
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    # second line
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    # third line
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def play(board):
    status = 'continue'
    player = 'X'

    while status == 'continue':
        square = int(input(f"{player}'s turn to choose a square (1-9):"))
        square -= 1
        if square < 0 and square > 0:
            print("invalid sqaure")
            continue
        board[square] = player
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
        print_board(board)
        if is_draw(board):
            status = 'draw'
        if has_winner(board):
            status = 'winner'

    print("Good game. Thanks for playing!")


def is_draw(board):
    for square in range(9):
        if board[square] != "X" and board[square] != "O":
            return False
    return True


def has_winner(board):
    # eval cases to win
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])


if __name__ == "__main__":
    main()
