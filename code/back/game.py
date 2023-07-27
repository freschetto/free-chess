"""
    This is our class for game engine function
"""

from code.back.board import Board


class Game:

    def __init__(self):
        # create bool and check if user has picked a piece
        self.selected_piece = None
        # create board to manage game
        self.board = Board()
        # create string for current team player
        self.player = 'w'

    # ------------------------------------------------------------------------------------------------------------------

    def change_player(self) -> str: return 'b' if self.player == 'w' else 'w'

    def change_state(self):
        self.selected_piece = None
        self.player = self.change_player()

    # ------------------------------------------------------------------------------------------------------------------

    def user_input(self, pos):

        if self.board.visual[pos[1]][pos[0]] != '  ':  # SELECT PIECE

            if self.selected_piece is None:  # PICK PIECE
                self.selected_piece = self.pick_piece(pos)

            elif self.board.is_enemy(self.selected_piece.name, pos) and self.valid_moves(pos):  # ATTACK
                self.attack_enemy(self.selected_piece, pos)

            else:  # CHANGE PIECE
                self.selected_piece = self.pick_piece(pos)

        elif self.selected_piece is not None and self.valid_moves(pos):  # MOVE
            self.move_piece(self.selected_piece, pos)

    # ------------------------------------------------------------------------------------------------------------------

    def valid_moves(self, pos):
        return pos in self.selected_piece.moves

    def pick_piece(self, pos):
        piece = self.board.pick_piece(pos)
        return piece if piece is not None and piece.name[0] == self.player else None

    def attack_enemy(self, piece, pos):
        self.board.remove_piece(pos)
        self.board.update(piece, pos)
        self.change_state()

    def move_piece(self, piece, pos):
        self.board.update(piece, pos)
        self.change_state()

    # ------------------------------------------------------------------------------------------------------------------
