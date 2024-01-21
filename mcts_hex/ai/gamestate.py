import numpy as np


class GameState:
    PLAYERS = {"none": 0, "white": 1, "black": 2}
    GAMEOVER = -1

    neighbor_patterns = ((-1, 0), (0, -1), (-1, 1), (0, 1), (1, 0), (1, -1))

    def __init__(self, size):
        self.size = size
        self.to_play = self.PLAYERS["white"]
        self.board = np.zeros((size, size))

    def play(self, cell):
        if self.to_play == self.PLAYERS["white"]:
            self.place_white(cell)
            self.to_play = self.PLAYERS["black"]
        elif self.to_play == self.PLAYERS["black"]:
            self.place_black(cell)
            self.to_play = self.PLAYERS["white"]

    def place_white(self, cell):
        if self.board[cell] == self.PLAYERS["none"]:
            self.board[cell] = self.PLAYERS["white"]
        else:
            print("Cell occupied")

    def place_black(self, cell):
        if self.board[cell] == self.PLAYERS["none"]:
            self.board[cell] = self.PLAYERS["black"]
        else:
            print("Cell occupied")

    def turn(self):
        return self.to_play

    def set_turn(self, player):
        if player in self.PLAYERS.values() and player != self.PLAYERS["none"]:
            self.to_play = player
        else:
            raise ValueError('Invalid turn: ' + str(player))

    def winner(self):
        visited = set()

        for edge_cell in range(self.size):
            if self.board[self.size - 1, edge_cell] == self.PLAYERS["white"]:
                if self.dfs((self.size - 1, edge_cell), visited, self.PLAYERS["white"]):
                    return self.PLAYERS["white"]

        for edge_cell in range(self.size):
            if self.board[edge_cell, self.size - 1] == self.PLAYERS["black"]:
                if self.dfs((edge_cell, self.size - 1), visited, self.PLAYERS["black"]):
                    return self.PLAYERS["black"]

        return self.PLAYERS["none"]

    def dfs(self, cell, visited, player):
        x, y = cell
        if x < 0 or x >= self.size or y < 0 or y >= self.size:
            return False

        if cell in visited or self.board[cell] != player:
            return False

        visited.add(cell)

        if player == self.PLAYERS["white"] and x == 0:
            return True
        elif player == self.PLAYERS["black"] and y == 0:
            return True

        for neighbor in self.neighbors(cell):
            if self.dfs(neighbor, visited, player):
                return True

        return False

    def neighbors(self, cell):
        x = cell[0]
        y = cell[1]
        return [(n[0] + x, n[1] + y) for n in self.neighbor_patterns \
                if (0 <= n[0] + x < self.size and 0 <= n[1] + y < self.size)]

    def moves(self):
        moves = []
        for y in range(self.size):
            for x in range(self.size):
                if self.board[x, y] == self.PLAYERS["none"]:
                    moves.append((x, y))
        return moves

    def __str__(self):
        white = 'O'
        black = '@'
        empty = '.'
        ret = '\n'
        coord_size = len(str(self.size))
        offset = 1
        ret += ' ' * (offset + 1)
        for x in range(self.size):
            ret += chr(ord('A') + x) + ' ' * offset * 2
        ret += '\n'
        for y in range(self.size):
            ret += str(y + 1) + ' ' * (offset * 2 + coord_size - len(str(y + 1)))
            for x in range(self.size):
                if self.board[x, y] == self.PLAYERS["white"]:
                    ret += white
                elif self.board[x, y] == self.PLAYERS["black"]:
                    ret += black
                else:
                    ret += empty
                ret += ' ' * offset * 2
            ret += white + "\n" + ' ' * offset * (y + 1)
        ret += ' ' * (offset * 2 + 1) + (black + ' ' * offset * 2) * self.size

        return ret
