from random import randint


class GameBoard:
    """ This is a class representing a tic-tac-toe gameboard.
    Parameters:
        board: The gameboard itself. Starting the indexing with 0,0 from the top
            left corner.
    Methods:
        print_board: Prints the current state of the board in a beautiful format.
        markCell: This method is used to mark a free cell. If the cell is taken,
            then the method fails.
    """

    def __init__(self):
        self.board = [[" " for i in range(3)] for j in range(3)]
        self.empty_cells = 9

    def print_board(self):
        for i, row in enumerate(self.board):
            print(" {} | {} | {} ".format(row[0], row[1], row[2]))
            if i != 2:
                print("-"*11)

    def markCell(self, mark, i, j):
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
            If the game continues, returns false.
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

        # Check if we have a tie.
        if self.empty_cells == 0:
            return "Tie"

        # No winner yet.
        return False


class Player:
    def __init__(self, name="Unnamed", mark="X"):
        self.set_name(name)
        self.set_mark(mark)

    def set_name(self, name):
        if name != "":
            self.name = name
        else:
            self.name = "Unnamed"

    def set_mark(self, mark):
        if mark != "":
            self.mark = mark
        else:
            self.mark = "X"


class TicTacToe:
    """ The tic-tac-toe game itself. It is consisted of the gameboard and the
            two players. It has the main gameloop that prompts the appropriate
            player for the row and col number each turn and checks for the ending
            of the game. If there is a winner, they get announced.
    """

    def __init__(self):
        self.players = [Player(mark="X"), Player(mark="O")]
        self.board = GameBoard()

    def gameloop(self):
        """ TODO: Check inputs for integers. """
        self.getPlayerInfo()
        p = self.coinFlip() # Flip coin for who plays first

        winner = False
        while not winner:
            print()
            self.board.print_board()
            print()

            i = j = -1
            while not self.board.markCell(self.players[p].mark, i, j):
                i = int( input("Player {} - Please enter the row number: ".format(p+1)) )
                while i > 3 or i < 0:
                    i = int( input("Player {} - Please enter a correct row number [0,2]: ".format(p+1)) )
                j = int ( input("Player {} - Please enter the column number: ".format(p+1)) )
                while j > 3 or j < 0:
                    j = int ( input("Player {} - Please enter a correct column number [0,2]: ".format(p+1)) )

            print()
            print("{} in cell: ({},{})".format(self.players[p].mark, i, j))
            p = (p + 1) % 2 # change to next player
            winner = self.board.checkWinner()

        # Game ended.
        print()
        self.board.print_board()

        if winner == "Tie":
            print("The game was a tie!")
        elif self.players[0].mark == winner:
            print("Congratulations player 1. You are the winner!")
        else:
            print("Congratulations player 2. You are the winner!")

    def getPlayerInfo(self):
        name = input("Player 1 please enter your name: ").strip(' \t\n\r')
        while name == "":
            name = input("Player 1 please enter a valid name: ").strip(' \t\n\r')
        self.players[0].set_name(name)

        name = input("Player 2 please enter your name: ").strip(' \t\n\r')
        while name == "" or name == self.players[0].name:
            if name == self.players[0].name:
                print("Your name is the same as player 1. Please enter a different name.")
            name = input("Player 2 please enter a valid name: ").strip(' \t\n\r')
        self.players[1].set_name(name)

    def coinFlip(self):
        """ Will be used in initialization to check who will play first. """
        coin = randint(0,1)
        return coin

    # Testing purposes
    def test_getPlayerInfo(self):
        self.getPlayerInfo()
        print("Player 1:", self.players[0].name)
        print("Player 2:", self.players[1].name)

    def test_coinFlip(self):
        for i in range(10):
            print(self.coinFlip())



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



if __name__ == '__main__':

    game = TicTacToe()
    # game.test_getPlayerInfo()
    game.gameloop()
    # p1 = Player("awd",'D')
    # players = [p1, Player(name="ed",mark="O")]
    # for i in range(2):
    #     print(players[i].name)
    #     print(players[i].mark)
    #
    # print (p1.name)
    # print(p1.mark)
