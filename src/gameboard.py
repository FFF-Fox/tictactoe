class GameBoard:
    """ This is the tic-tac-toe gameboard.
    Parameters:
        board: The gameboard itself. Starting the indexing with 0,0 from the top
            left corner.
    Methods:
        print_board: Prints the current state of the board in a beautiful format.
        markCell: This method is used to mark a free cell. If the cell is taken,
            then the method fails.
        clear_board: Clears the board from any marks.
    """

    def __init__(self):
        self.board = [[" " for i in range(3)] for j in range(3)] # " " represents the empty cell
        self.empty_cells = 9

    def print_board(self):
        print("   {}   {}   {} ".format(0, 1, 2))
        for i, row in enumerate(self.board):
            print("{}  {} | {} | {} ".format((i), row[0], row[1], row[2]))
            if i != 2:
                print("  "+"-"*11) # Uses "  " to align with the board.

    def markCell(self, mark, i, j):
        """ Mark the cell (i,j) with mark. Returns true/false whether the
                marking was succesful.

            Parameters:
                mark: String.
                i: int. The board's row number.
                j: int. The board's col number.
        """
        if 0 <= i < len(self.board) and 0 <= j < len(self.board) and self.empty_cells > 0:
            if self.board[i][j] != " ":
                return False
            else:
                self.board[i][j] = mark
                self.empty_cells -= 1
                return True
        else:
            return False

    def checkWinner(self):
        """ Checks the board for winner or tie.
            If there is a winner, returns the winner's mark.
            If there is a tie, returns "Tie".
            If none of these end conditions is met, returns None.
        """

        # Check horizontal and vertical lines.
        for j in range(3):
            if self.board[0][j] != " " and self.board[0][j] == self.board[1][j] == self.board[2][j]:
                return self.board[0][j]
            if self.board[j][0] != " " and self.board[j][0] == self.board[j][1] == self.board[j][2]:
                return self.board[j][0]

        # Check diagonals.
        if self.board[0][0] != " " and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        elif self.board[0][2] != " " and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[0][2]

        # Check if there is a tie.
        if self.empty_cells == 0:
            return "Tie"

        # No winner yet.
        return None


# GameBoard tests.

def test_markCell():
    board = GameBoard()
    if board.markCell("X", 0, 0):
        board.print_board()
        print()
    if board.markCell("O", 1, 0):
        board.print_board()
        print()
    if not board.markCell("X", 1, 0):
        board.print_board()
        print()
    if not board.markCell("O", 5, 0):
        board.print_board()
        print()

def test_checkWinner():
    board = [GameBoard() for i in range(6)]

    for i in range(3):
        board[0].markCell("X", 0, i)
        board[1].markCell("O", i, 0)
        board[2].markCell("X", i, i)
        board[3].markCell("O", i, 2-i)

    # Tie
    for i in range(3):
        for j in range(3):
            board[4].markCell("{}".format(j+i*2), i, j)

    board[5].markCell("X", 0, 1)

    for b in board:
        b.print_board()
        print(b.checkWinner())
