# -*- coding: utf8 -*-

from collections import deque
from copy import deepcopy

from PyQt5.QtCore import QRunnable

from board import Board


class Simulator(QRunnable):
    def __init__(self, init_board, signal):
        super(Simulator, self).__init__()
        self.history = set()
        self.queue = deque()
        self.answer = None
        self.signal = signal

        init_board = Board([_ for _ in map(int, init_board)])
        self.history.add(hash(init_board))
        self.queue.append(init_board)

    def run(self):
        while self.answer is None:
            cnt = len(self.queue)
            last_cnt = len(self.history)
            while cnt:
                cnt -= 1
                board = self.queue.popleft()
                for index in range(6):
                    new_board = deepcopy(board)
                    new_board.rotate(index)
                    if new_board.is_result():
                        self.answer = new_board
                        break
                    if hash(new_board) in self.history:
                        continue
                    self.history.add(hash(new_board))
                    self.queue.append(new_board)
            if last_cnt == len(self.history):
                break

        if self.answer is None:
            self.signal.emit("")
        else:
            self.signal.emit(str(self.answer.ops))
