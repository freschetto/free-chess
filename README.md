# ♟️ CHESS AI

This is a simple chess game implemented in Python using the pygame library.

![EXAMPLE](info/game_example.png)

## ⚙️ INSTALLATION

-  `[ Pygame ]` `[ Python 3.X ]`

1. **Clone the repository**:

```
git clone https://github.com/freschetto/free-chess.git
```

2. **Create Virtual Environment (optional)**:
```
python3 -m venv env_name
```

- Activate on Linux / macOS:  `source env_name/bin/activate`
- On Windows:  `env_name\Scripts\activate`

3. **Install the required dependencies**: 
```
pip install -r requirements.txt
```

## 🎮 USAGE

1. Run the main.py file to start the game: `python main.py`

2. The game window will open, displaying the chessboard.

3. Players can take turns selecting and moving their pieces using the mouse.

4. The game follows standard chess rules.

5. The game will continue until one player is checkmated or a draw is reached.

## 🗂️ UML

![UML](info/uml_image.jpeg)

## 🔍 ROADMAP

**STEP 01**
- Data structure to represent the chessboard
- Classes for different chess pieces
- Implement logic to generate all possible legal moves for each piece

**STEP 02**
- Create game engine for board changes
- Develop a graphical user interface to display the chessboard (GUI)
- Allow players to make moves using mouse clicks (GUI)

**STEP 03**
- Implement logic to check for checks and checkmates 
- Validate pieces moves if is checkmate (remove from legal moves)

**STEP 04**
- Build en passant and promotion for pawns
- Build castling for kings and rooks

**STEP 05**
- Implement a winning condition (capturing the opponent's king or a draw)
- Create a game loop that handles player moves and updates the board accordingly until the game ends

## 📄 LICENSE

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). See the `LICENSE` file for more details.
