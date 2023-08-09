"""
    This is our class for pieces in game
"""
import copy


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

    def check(self, board):
        pos = self.pos
        invalid_moves = []
        for move in self.moves:
            two = copy.deepcopy(board)
            if two.is_enemy(self.name, move):
                two.remove_piece(move)
            two.update(self, move)
            if two.is_check(self.name[0]):
                invalid_moves.append(move)
            self.pos = pos
        for invalid in invalid_moves:
            self.moves.remove(invalid)

    def update(self, board):
        self.moves = self.valid_moves(board)
