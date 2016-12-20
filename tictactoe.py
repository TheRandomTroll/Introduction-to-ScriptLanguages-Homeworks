def player_input():
    pass


def check_win():
    pass


def print_board(board):
    print('-' * 9, end='')
    for row in board:
        print()
        print(*row, sep=' | ', end='\n' + '-' * 9)
    print()


def main():
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
    ]

    print_board(board)


if __name__ == '__main__':
    main()
