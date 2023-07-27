"""
    This is our test class for back-end
"""

from game import Game


def print_board(board):  # VISUALIZE BOARD ON CONSOLE

    print()
    print("-------------------------------------")

    for row in board.visual:
        for element in row:
            print(element, end=' ')
        print()

    print("-------------------------------------")
    print()


game = Game()

while True:

    print_board(game.board)

    x, y = input("INSERT POSITION: ").split()
    game.user_input((int(x), int(y)))

    print()
    print("PIECE: " + game.selected_piece.name, game.selected_piece.moves) if game.selected_piece is not None else print("SELECT A PIECE")
    print()

