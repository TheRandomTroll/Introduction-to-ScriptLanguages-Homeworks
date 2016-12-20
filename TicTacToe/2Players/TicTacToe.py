import sys


def tictactoe_2_players():
    def print_board(board):
        for row in board:
            print(row)


    board = [
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']
    ]

    player = 'X'
    opponent = 'O'

    while True:
        player_1 = map(int, input("Enter player 1's input coordinates (separated by space): ").split(' '))
        if board[player_1[0]][player_1[1]] != '-':
            board[player_1[0]][player_1[1]] = player
            print_board(board)
            break
        else:
            print("The current cell is already occupied. Enter different coordinates.")

    while True:
        player_1 = map(int, input("Enter player 2's input coordinates (separated by space): ").split(' '))
        if board[player_1[0]][player_1[1]] != '-':
            board[player_1[0]][player_1[1]] = opponent
            print_board(board)
            break
        else:
            print("The current cell is already occupied. Enter different coordinates.")

            
def main():
    pass

if __name__ == "__main__":
    sys.exit(int(main() or 0))