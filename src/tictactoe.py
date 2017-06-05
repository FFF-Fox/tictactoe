from random import randint
import string

from player import Player
from gameboard import GameBoard


class TicTacToe:
    """ The tic-tac-toe game itself. It is consisted of the gameboard and the
            two players. It has the main gameloop that prompts the appropriate
            player for the row and col number each turn and checks for the ending
            of the game. If there is a winner, they get announced.
    """

    def __init__(self):
        self.players = [Player(mark="X"), Player(mark="O")]
        self.board = GameBoard()

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

        winner = None
        while winner is None:
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


# Testing Functions

# TicTacToe tests.

def test_getPlayerInfo():
    game = TicTacToe()
    game.getPlayerInfo()

    # Maybe use assert statements?
    print("Player 1:", game.players[0].name)
    print("Player 2:", game.players[1].name)

def test_coinFlip():
    game = TicTacToe()
    for i in range(10):
        print(game.coinFlip())

def test_gameloop():
    # Need to find a proper test for this function.
    pass


if __name__ == '__main__':

    game = TicTacToe()

    # ---------- Tests ---------- #

    # test_getPlayerInfo()
    # test_coinFlip()

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
