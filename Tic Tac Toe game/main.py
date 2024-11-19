import random


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

    def display_board(self):
        for i in range(0, 9, 3):
            print(f' {self.board[i]} | {self.board[i + 1]} | {self.board[i + 2]} ')
            if i < 6:
                print('-----------')

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            return True
        return False

    def check_winner(self):
        # Winning combinations
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]

        for combo in win_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' '):
                return self.board[combo[0]]

        if ' ' not in self.board:
            return 'Tie'

        return None

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play(self):
        print("Welcome to Tic Tac Toe!")
        while True:
            self.display_board()
            print(f"Player {self.current_player}'s turn")

            try:
                move = int(input("Enter position (0-8): "))
                if move < 0 or move > 8:
                    print("Invalid position. Try again.")
                    continue

                if self.make_move(move):
                    winner = self.check_winner()
                    if winner:
                        self.display_board()
                        if winner == 'Tie':
                            print("It's a tie!")
                        else:
                            print(f"Player {winner} wins!")
                        break

                    self.switch_player()
                else:
                    print("Position already occupied. Try again.")

            except ValueError:
                print("Please enter a valid number.")


def main():
    game = TicTacToe()
    game.play()


if __name__ == "__main__":
    main()