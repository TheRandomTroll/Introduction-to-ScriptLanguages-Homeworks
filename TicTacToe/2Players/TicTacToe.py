import sys


def tictactoe_2_players():
    def print_board(board):
        print('   |   |')
        print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
        print('   |   |')


    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

    print_board(board)
    player = 'X'
    opponent = 'O'

    def getPlayerMove(board):
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
            print('What is your next move? (1-9)')
            move = input()
        return int(move) - 1


    def isSpaceFree(board, coord):
        return board[coord] == ' '
    

    def is_board_full(board):
     for i in range(0, 9):
         if isSpaceFree(board, i):
             return False
     return True


def main():
    tictactoe_2_players()

if __name__ == "__main__":
    sys.exit(int(main() or 0))