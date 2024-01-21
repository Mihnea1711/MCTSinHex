class Utils:
    ABOUT_PAGE = """
    ==============================================
                    About Hex Game
    ==============================================
    Hex is a two-player connection board game. The 
    objective is to connect your sides of the board 
    with a continuous path of your pieces.

    Playing vs Friend:
    - Select 'Play Vs Friend' from the main menu.
    - Take turns placing your pieces on the board.
    - The first player to create a connecting path wins.

    Playing vs AI (MCTS Agent):
    - Select 'Play vs AI' from the new game menu.
    - The AI uses Monte Carlo Tree Search (MCTS).
    - It simulates random games to find the best move.
    - Be prepared for a challenging game against the AI!
    ==============================================
                    Hex Game Rules
    ==============================================
    Hex is played on a hexagonal grid. The goal is
    to connect two opposite sides of the board with
    a continuous path of your colored pieces.

    Gameplay:
    1. Players take turns placing their pieces on
       empty hexagonal spaces on the board.
    2. The first player to create a connecting path
       from one side to the opposite side wins.

    Rules:
    - Diagonal connections are allowed.
    - Pieces cannot be moved once placed.
    - Blocking your opponent's path is crucial.
    - The game ends when a connection is formed.
    - Enjoy the strategic and challenging gameplay!
    ==============================================
    """

    NAME = "name"
    LIST_COMMANDS = "list_commands"
    SHOW_BOARD = "showboard"
    CLEAR_BOARD = "clear_board"
    PLAY = "play"
    GENMOVE = "genmove"
    QUIT = "quit"

    PLAYER_WHITE = "WHITE"
    PLAYER_BLACK = "BLACK"
    PLAYER = "PLAYER"
    PLAYER_AI = "AI"

    WINNER_NONE = 0
    WINNER_WHITE = 1
    WINNER_BLACK = 2

    WINNER_MESSAGES = {
        WINNER_NONE: "",
        WINNER_WHITE: "Player WHITE wins!",
        WINNER_BLACK: "Player BLACK wins!"
    }