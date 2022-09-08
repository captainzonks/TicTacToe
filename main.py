import numpy as np

board = [['1', '2', '3'],
         ['4', '5', '6'],
         ['7', '8', '9']]


def display_board(board):
    for row in board:
        print(row)


def check_rows(board):
    for row in board:
        # convert the list into a set to check if the length is 1
        if len(set(row)) == 1:
            # if it is, then that means all values are the same, and thus a win
            return row[0]
    return 0


def check_diagonals(board):
    # check board[0][0], board[1][1], and board[2][2] as a set for length of 1
    if len(set([board[i][i] for i in range(len(board))])) == 1:
        # if found, win
        return board[0][0]
    # check the other diagonal for a set length of 1
    if len(set([board[i][len(board) - i - 1] for i in range(len(board))])) == 1:
        # if found, win
        return board[0][len(board) - 1]
    return 0


def check_win(board):
    # transposition to check rows, then columns
    for new_board in [board, np.transpose(board)]:
        result = check_rows(new_board)
        if result:
            return result
    return check_diagonals(board)


def get_user_input():
    row = input("Please enter a row number: ")
    column = input("Please enter a column number: ")
    return int(row)-1, int(column)-1


def submit_user_input(player, user_input):
    board[user_input[0]][user_input[1]] = player


# Main loop
display_board(board)
player = 'X'
while True:
    user_input = get_user_input()
    submit_user_input(player, user_input)
    display_board(board)
    if check_win(board) != 0:
        print(f"Player {player} wins!")
        break

    if player == 'X':
        player = 'O'
    else:
        player = 'X'
