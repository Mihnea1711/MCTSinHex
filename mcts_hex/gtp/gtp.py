from ai.gamestate import GameState
from ai.agent import Agent
from utils.utils import Utils


class GTP:
    def __init__(self, board_size, difficulty):
        commands = {
            Utils.NAME: self.gtp_name,
            Utils.LIST_COMMANDS: self.gtp_list,
            Utils.SHOW_BOARD: self.gtp_show,
            Utils.CLEAR_BOARD: self.gtp_clear,
            Utils.PLAY: self.gtp_play,
            Utils.GENMOVE: self.gtp_gen_move,
            Utils.QUIT: self.gtp_quit
        }

        self.commands = commands
        self.board_size = board_size
        self.difficulty = difficulty

        self.game = GameState(self.board_size)
        self.agent = Agent(difficulty)
        self.agent.set_game_state(self.game)

    def set_board_size(self, board_size):
        self.board_size = board_size
        self.game = GameState(board_size)

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty

    def get_winner(self):
        return self.game.winner()

    def send_command(self, command):
        parsed_command = command.split()
        name = parsed_command[0].strip()
        args = parsed_command[1:]
        if name in self.commands:
            return self.commands[name](args)
        else:
            return False, "Unrecognized command"

    @staticmethod
    def gtp_name():
        return True, "HEX"

    def gtp_list(self):
        ret = ''
        for command in self.commands:
            ret += '\n' + command
        return True, ret

    @staticmethod
    def gtp_quit(args):
        exit()

    def gtp_clear(self, args):
        self.game = GameState(self.game.size)
        self.agent.set_game_state(self.game)
        return True, ""

    def gtp_play(self, args):
        if len(args) < 2:
            return False, "Not enough arguments"
        try:
            x = ord(args[1][0].lower()) - ord('a')
            y = int(args[1][1:]) - 1

            if x < 0 or y < 0 or x >= self.game.size or y >= self.game.size:
                return False, "Cell out of bounds"

            if args[0].upper() == Utils.PLAYER_WHITE:
                if self.game.turn() == GameState.PLAYERS["white"]:
                    self.game.play((x, y))
                    self.agent.move((x, y))
                    return True, ""
                else:
                    self.game.place_white((x, y))
                    self.agent.set_game_state(self.game)
                    return True, ""

            elif args[0].upper() == Utils.PLAYER_BLACK:
                if self.game.turn() == GameState.PLAYERS["black"]:
                    self.game.play((x, y))
                    self.agent.move((x, y))
                    return True, ""
                else:
                    self.game.place_black((x, y))
                    self.agent.set_game_state(self.game)
                    return True, ""

            else:
                return False, "Player not recognized"

        except ValueError:
            return False, "Malformed arguments"

    def gtp_gen_move(self, args):
        if len(args) > 0:
            if args[0][0].lower() == 'w':
                if self.game.turn() != GameState.PLAYERS["white"]:
                    self.game.set_turn(GameState.PLAYERS["white"])
                    self.agent.set_game_state(self.game)

            elif args[0][0].lower() == 'b':
                if self.game.turn() != GameState.PLAYERS["black"]:
                    self.game.set_turn(GameState.PLAYERS["black"])
                    self.agent.set_game_state(self.game)
            else:
                return False, "Player not recognized"

        self.agent.search()
        move = self.agent.best_move()

        if move == GameState.GAMEOVER:
            return False, "The game is already over"
        self.game.play(move)
        self.agent.move(move)
        return True, chr(ord('a') + move[0]) + str(move[1] + 1)

    def gtp_show(self, args):
        return True, str(self.game)