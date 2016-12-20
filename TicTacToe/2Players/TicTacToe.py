import sys


def tictactoe_2_players():
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player = 'X'
    opponent = 'O'
    gameIsPlaying = True

    def make_player_move(board, player):
        print_board(board)
        move = get_player_move(board, player)
        make_move(board, player, move)
        nonlocal gameIsPlaying

        if is_winner(board, player):
            print_board(board)
            print('Hooray! %s wins!' % player)
            gameIsPlaying = False

        elif is_board_full(board):
            print_board(board)
            print('The game is a tie!')
            gameIsPlaying = False

    def print_board(board):
        print()
        print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
        print('-----------')
        print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
        print('-----------')
        print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
        print()


    def get_player_move(board, player):
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(move) - 1):
            move = input('It\'s %s\'s turn. Enter a number (1-9): ' % player)
        return int(move) - 1


    def is_winner(board, player):
        return (board[0] == player and board[1] == player and board[2] == player) or \
               (board[3] == player and board[4] == player and board[5] == player) or \
               (board[6] == player and board[7] == player and board[8] == player) or \
               (board[0] == player and board[3] == player and board[6] == player) or \
               (board[1] == player and board[4] == player and board[7] == player) or \
               (board[2] == player and board[5] == player and board[8] == player) or \
               (board[0] == player and board[4] == player and board[8] == player) or \
               (board[2] == player and board[4] == player and board[6] == player)


    def is_space_free(board, coord):
        return board[coord] == ' '


    def is_board_full(board):
     for i in range(0, 9):
         if is_space_free(board, i):
             return False
     return True
    
    def make_move(board, char, move):
        board[move] = char


    while gameIsPlaying:
        make_player_move(board, player)
        if gameIsPlaying:
            make_player_move(board, opponent)


def main():
    tictactoe_2_players()

if __name__ == "__main__":
    sys.exit(int(main() or 0))