from math import sqrt, log


class Node:
    def __init__(self, move=None, parent=None):
        self.move = move
        self.parent = parent
        self.times_visited = 0
        self.average_reward = 0
        self.children = []

    def add_children(self, children):
        self.children += children

    def uct_value(self, explore):
        if self.times_visited == 0:
            return 0 if explore == 0 else float('inf')
        return self.average_reward / self.times_visited + explore * sqrt(2 * log(self.parent.times_visited) / self.times_visited)
