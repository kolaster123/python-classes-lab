class Game:
    def __init__(self):
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }

    def print_board(self):
        b = self.board
        print(f"""
            A   B   C
        1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
            ----------
        2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
            ----------
        3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)

    def print_message(self):
        if self.tie:
            print("Tie game!")
        elif self.winner:
            print(f"{self.winner} wins the game!")
        else:
            print(f"It's player {self.turn}'s turn!")

    def render(self):
        self.print_board()
        self.print_message()

    def get_move(self):
        while True:
            move = input("Enter a valid move (example: A1): ").lower()
            if move in self.board and self.board[move] is None:
                self.board[move] = self.turn
                break
            else:
                print("Invalid move. Please try again.")

    def check_for_winner(self):
        b = self.board
        win_conditions = [
            ['a1', 'b1', 'c1'],  # Top 
            ['a2', 'b2', 'c2'],  # Middle 
            ['a3', 'b3', 'c3'],  # Bottom 
            ['a1', 'a2', 'a3'],  # Left 
            ['b1', 'b2', 'b3'],  # Middle 
            ['c1', 'c2', 'c3'],  # Right 
            ['a1', 'b2', 'c3'],  # Diagonal 
            ['c1', 'b2', 'a3']   # Diagonal 
        ]
        for condition in win_conditions:
            if b[condition[0]] and b[condition[0]] == b[condition[1]] == b[condition[2]]:
                self.winner = self.turn
                return

    def check_for_tie(self):
        if all(value is not None for value in self.board.values()) and not self.winner:
            self.tie = True

    def switch_turn(self):
        self.turn = 'O' if self.turn == 'X' else 'X'

    def play_game(self):
        print("Shall we play a game?")
        while not self.winner and not self.tie:
            self.render()
            self.get_move()
            self.check_for_winner()
            self.check_for_tie()
            if not self.winner and not self.tie:
                self.switch_turn()
        self.render()


game = Game()
game.play_game()
