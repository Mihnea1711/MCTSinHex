from enum import Enum

from gtp.gtp import GTP
from utils.utils import Utils


class Difficulty(Enum):
    EASY = 1
    NORMAL = 2
    HARD = 3

    def map_to_value(self):
        difficulty_mapping = {
            Difficulty.EASY: 0.5,
            Difficulty.NORMAL: 1,
            Difficulty.HARD: 1.5
        }
        return difficulty_mapping.get(self, 1)


class GameManager:
    def __init__(self):
        self.board_size: int = 5
        self.difficulty = Difficulty.NORMAL
        self.gtp = GTP(self.board_size, self.difficulty.map_to_value())

    def set_board_size(self, size):
        self.board_size = size
        self.gtp.set_board_size(size)

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty
        self.set_difficulty(difficulty)

    @staticmethod
    def print_command_response(success, response):
        if success:
            print(f"{response}\n")
        else:
            print(f"An error occurred: {response}\n")

    def display_board(self):
        success, response = self.gtp.send_command(Utils.SHOW_BOARD)
        self.print_command_response(success, response)

    def process_move(self, player_color):
        while True:
            prompt = f"Waiting for {player_color} to move: "
            command = input(prompt)
            if command.lower().strip().startswith(Utils.PLAY):
                args = command.split(" ")
                command = f"{args[0].strip()} {player_color} {args[1].strip().upper()}"
            success, response = self.gtp.send_command(command)
            self.print_command_response(success, response)
            if command.lower().strip().startswith(Utils.PLAY) and success:
                break
            if command.lower().strip().startswith(Utils.QUIT) and success:
                exit()

    def play_vs_player(self):
        self.gtp.send_command(Utils.CLEAR_BOARD)
        print(f"Player {Utils.PLAYER_WHITE} starts")
        is_white_turn = True

        while self.gtp.get_winner() == Utils.WINNER_NONE:
            player_color = Utils.PLAYER_WHITE if is_white_turn else Utils.PLAYER_BLACK
            self.display_board()
            self.process_move(player_color)
            is_white_turn = not is_white_turn

        winner_message = Utils.WINNER_MESSAGES[self.gtp.get_winner()]
        print(winner_message)

        self.gtp.send_command(Utils.SHOW_BOARD)

    def play_vs_ai(self):
        self.gtp.send_command(Utils.CLEAR_BOARD)
        print("\nYou start!")
        while self.gtp.get_winner() == Utils.WINNER_NONE:
            self.display_board()
            self.process_move(Utils.PLAYER_WHITE)

            # play ai
            print(f"Waiting for {Utils.PLAYER_AI} to move...")
            self.gtp.send_command(f"{Utils.GENMOVE} black")

        winner = self.gtp.get_winner()
        if winner == Utils.WINNER_WHITE:
            winner_message = "You win!"
        elif winner == Utils.WINNER_BLACK:
            winner_message = "You lose!"
        else:
            winner_message = "It's a draw!"
        print(winner_message)

        self.gtp.send_command(Utils.SHOW_BOARD)

    def show_commands(self):
        print("\nDisplaying available commands...")
        self.gtp.gtp_list()

