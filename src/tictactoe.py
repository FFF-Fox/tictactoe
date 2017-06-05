from random import randint
import string


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
            If none of these end conditions is met, returns false.
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
        return False


class Player:
    """ A class representing the player in the tic-tac-toe game.
    Attributes:
        name: String. The nickname of the player. Single word is allowed.
        mark: String. The mark eg.:('x' or 'o') of this player. Should be a
            single character in length. Whitespace is not allowed.
    """
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
        """ The main game loop. Controls the flow of the game.
                1. Gets the players names.
                2. Flips a coin to decide which player goes first.
                3. On each turn check whether there is a winner.
                    If there is not, show the board and prompt the player to
                    enter the row and col numbers of the spot that they want
                    marked.
        """

        # Game initialization.

        self.getPlayerInfo()
        p = self.coinFlip()     # Flip coin to decide who plays first.

        # The main loop.

        winner = False
        while not winner:
            print()
            self.board.print_board()
            print()

            # Check input for each turn.

            # Row checks.

            i = j = -1  # init i,j to an invalid value.
            while not self.board.markCell(self.players[p].mark, i, j):
                i_set = False   # used to check whether i is set correctly.
                while not i_set:
                    i = input("{} - Please enter the row number: ".format(self.players[p].name))
                    if i.isdigit():
                        i = int(i)
                        # check if it is within range.
                        if 0 <= i <= 2:
                            i_set = True
                        else:
                            print("The choice you have entered is out of bounds.")
                            print("Please enter an integer from 0 to 2.")
                    else:
                        # i is not a digit.
                        print("Please enter an integer from 0 to 2.")

                # Column checks.

                j_set = False   # used to check whether j is set correctly.
                while not j_set:
                    j = input("{} - Please enter the column number: ".format(self.players[p].name))
                    if j.isdigit():
                        j = int(j)
                        # check if it is within range.
                        if 0 <= j <= 2:
                            j_set = True
                        else:
                            print("The choice you have entered is out of bounds.")
                            print("Please enter an integer from 0 to 2.")
                    else:
                        # j is not a digit.
                        print("Please enter an integer from 0 to 2.")

            print()
            print("{} placed in cell: ({},{})".format(self.players[p].mark, i, j))

            p = (p + 1) % 2     # Change to next player.
            winner = self.board.checkWinner()

        # Game ended.

        print()
        self.board.print_board()

        if winner == "Tie":
            print("The game was a tie!")
        elif self.players[0].mark == winner:
            print("Congratulations {}. You are the winner!".format(self.players[0].name))
        else:
            print("Congratulations {}. You are the winner!".format(self.players[1].name))

    def getPlayerInfo(self):
        """ Get both the players' names. The names are striped of whitespaces.
            The two players are not allowed to have the same names, an empty
            name or names containing punctuation.
        """

        # Add whitespace to the invalid chars.
        invalidChars = set(string.punctuation + " ")

        # Player 1

        name = input("Player 1 please enter your name: ").strip(' \t\n\r')
        while name == "" or any(char in invalidChars for char in name):
            name = input("Player 1 please enter a valid name: ").strip(' \t\n\r')
        self.players[0].set_name(name)

        # Player 2

        name = input("Player 2 please enter your name: ").strip(' \t\n\r')
        while (name == ""
              or name == self.players[0].name
              or any(char in invalidChars for char in name)):
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

    # ---------- Tests ---------- #

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

    # print("2 :","2".isdigit())
    # print("awd :","awd".isdigit())
    # print("-2 :","-2".isdigit())
    # print("22 :","22".isdigit())
    # print("0 :","0".isdigit())
    # print("2.2 :","2.2".isdigit())
