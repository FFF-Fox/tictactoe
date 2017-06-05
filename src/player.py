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


# Player tests.

def test_set_name():
    # Need to find some tests for this function.
    pass

def test_set_mark():
    # Need to find some tests for this function.
    pass
