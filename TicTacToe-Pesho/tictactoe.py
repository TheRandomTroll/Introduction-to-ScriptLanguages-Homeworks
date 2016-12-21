# Next step: combine functions into a class

def print_board(board):
    print('-' * 9, end='')
    for row in board:
        print()
        print(*row, sep=' | ', end='\n' + '-' * 9)
    print()


def player_turn(board, player):
    print("Current board: ")
    print_board(board)

    while True:
        print("Please enter the row and column")
        row = int(input("row (1-3): "))
        column = int(input("column (1-3): "))

        # Check if the position is valid and not occupied
        if 1 <= row <= 3 and 1 <= column <= 3 and \
                board[row-1][column-1] == ' ':
            break

    board[row-1][column-1] = player


def check_win(board, player, player_pos):
    # player_pos = (row, column)
    row_pos = player_pos[0]
    column_pos = player_pos[1]

    column = board[0][column_pos], board[1][column_pos], board[2][column_pos]
    diagonal_1 = board[0][2], board[1][1], board[2][0]
    diagonal_2 = board[0][0], board[1][1], board[2][2]

    if all(pos == player for pos in diagonal_1) or \
            all(pos == player for pos in diagonal_2) or \
            all(pos == player for pos in board[row_pos]) or \
            all(pos == player for pos in column):
        return True
    return False


def main():
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
    ]

    player_turn(board, 'x')

    print("End of game")
    print_board(board)


if __name__ == '__main__':
    main()
