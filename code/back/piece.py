"""
    This is our class for pieces in game
"""


class Piece:

    def __init__(self, name, pos):
        # create string that contain color + type
        self.name = name
        # create tuple for piece position on the board
        self.pos = pos
        # create list for legal moves
        self.moves = []

    # ----------------------------------------------------------------------------------------------------------------

    def valid_moves(self, board): pass

    # ----------------------------------------------------------------------------------------------------------------

    def update(self, pos, board):
        # change piece position
        self.pos = pos
        # calculate all valid moves with new position
        self.moves = self.valid_moves(board)
