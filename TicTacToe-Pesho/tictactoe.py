class TicTacToeGame:
    def __init__(self):
        self.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
        ]

    def __str__(self):
        _board = '-'*13 + '\n'

        for row in self.board:
            _board += '| '
            for element in row:
                _board += element + ' | '
            _board += '\n' + '-'*13 + '\n'

        return _board

    def player_turn(self, player):
        print("\n%s's turn..." % player)
        print("Current board: ")
        print(self)

        while True:
            print("Please enter the row and column")
            row = int(input("row (1-3): "))
            column = int(input("column (1-3): "))

            # Check if the position is valid and not occupied
            if 1 <= row <= 3 and 1 <= column <= 3 and \
                    self.board[row-1][column-1] == ' ':
                break

        self.board[row-1][column-1] = player
        return row-1, column-1  # return player_pos that is required for check_win

    def check_win(self, player, player_pos):
        row_pos = player_pos[0]
        column_pos = player_pos[1]

        column = self.board[0][column_pos], self.board[1][column_pos], self.board[2][column_pos]
        diagonal_1 = self.board[0][2], self.board[1][1], self.board[2][0]
        diagonal_2 = self.board[0][0], self.board[1][1], self.board[2][2]

        # First check the diagonals, then - row and column
        if all(pos == player for pos in diagonal_1) or \
                all(pos == player for pos in diagonal_2) or \
                all(pos == player for pos in self.board[row_pos]) or \
                all(pos == player for pos in column):
            return True
        return False

    def play_game(self, player=''):
        player = 'x' if player != 'x' else 'o'
        player_pos = self.player_turn(player)

        if self.check_win(player, player_pos):
            print("\nGame over...")
            print(self)
            print("And the winner is: '%s'. Congratulations!" % player)
            return player
        else:
            self.play_game(player)


def main():
    game_1v1 = TicTacToeGame()
    game_1v1.play_game()


if __name__ == '__main__':
    main()
