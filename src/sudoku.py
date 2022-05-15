from math import sqrt
from random import sample
from copy import deepcopy


class Sudoku:
    board = []

    def __init__(self, size: int = 9):
        self.size = size
        self.base = sqrt(size)
        if not self.base.is_integer():
            raise SudokuException()
        self.base = int(self.base)
        self.board = self.generate()

    def pattern(self, r, c):
        return int((self.base * (r % self.base) + r // self.base + c) % self.size)

    @staticmethod
    def shuffle(s):
        return sample(s, len(s))

    def generate(self):
        r_base = range(self.base)
        rows = [g * self.base + r for g in self.shuffle(r_base) for r in self.shuffle(r_base)]
        cols = [g * self.base + c for g in self.shuffle(r_base) for c in self.shuffle(r_base)]
        nums = self.shuffle(range(1, int(self.base * self.base + 1)))
        board = [[nums[self.pattern(r, c)] for c in cols] for r in rows]
        return board

    def get(self):
        return self.board

    def get_game(self):
        squares = self.size * self.size
        empties = squares * 3 // 4
        board = deepcopy(self.board)
        for p in sample(range(squares), empties):
            board[p // self.size][p % self.size] = 0
        return board

    def new_game(self):
        self.generate()
        return self.get_game()


class SudokuException(Exception):
    message = "size must be sqrt able."
