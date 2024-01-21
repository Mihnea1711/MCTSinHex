import random
import time
from copy import deepcopy

from ai.gamestate import GameState
from ai.node import Node


class Agent:
    EXPLORATION = 1

    def __init__(self, difficulty):
        self.root_state = None
        self.root = Node()
        self.difficulty = difficulty
        self.max_time = 5 * difficulty
        print("Initialized MCTS Agent")

    def best_move(self):
        if self.root_state.winner() != GameState.PLAYERS["none"]:
            return GameState.GAMEOVER

        max_value = max(self.root.children, key=lambda n: n.times_visited).times_visited
        max_nodes = [n for n in self.root.children if n.times_visited == max_value]
        return random.choice(max_nodes).move

    def move(self, move):
        child = next((child for child in self.root.children if move == child.move), None)
        self.root = child if child else Node()
        self.root_state.play(move)

    def search(self):
        start_time = time.time()
        num_rollouts = 0

        while time.time() - start_time < self.max_time:
            node, state = self.select_node()
            turn = state.turn()
            outcome = self.roll_out(state)
            self.backup(node, turn, outcome)
            num_rollouts += 1

        elapsed_time = time.time() - start_time
        print(f"{num_rollouts} rollouts\n {elapsed_time:.3f} sec")

    def select_node(self):
        node = self.root
        state = deepcopy(self.root_state)

        while node.children:
            max_value = max(node.children, key=lambda n: n.uct_value(self.get_exploration())).uct_value(
                self.get_exploration())
            max_nodes = [n for n in node.children if n.uct_value(self.get_exploration()) == max_value]
            node = random.choice(max_nodes)
            state.play(node.move)

            if node.times_visited == 0:
                return node, state

        if self.expand(node, state):
            node = random.choice(node.children)
            state.play(node.move)
        return node, state

    @staticmethod
    def roll_out(state):
        moves = state.moves()

        while state.winner() == GameState.PLAYERS["none"]:
            move = random.choice(moves)
            state.play(move)
            moves.remove(move)

        return state.winner()

    @staticmethod
    def backup(node, turn, outcome):
        reward = -1 if outcome == turn else 1

        while node:
            node.times_visited += 1
            node.average_reward += reward
            reward = -reward
            node = node.parent

    @staticmethod
    def expand(parent, state):
        if state.winner() != GameState.PLAYERS["none"]:
            return False

        children = [Node(move, parent) for move in state.moves()]
        parent.add_children(children)
        return True

    def set_game_state(self, state):
        self.root_state = deepcopy(state)
        self.root = Node()

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty

    def get_exploration(self):
        return self.difficulty * Agent.EXPLORATION
