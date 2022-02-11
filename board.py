# -*- coding: utf8 -*-

class Board(object):
    def __init__(self, init_board):
        self.board = init_board
        self.ops = list()

    def __hash__(self):
        ret = 0
        for i in range(12):
            ret += pow(12, i) * self.board[i]
        return ret

    def is_result(self):
        for i in range(12):
            if self.board[i] != i + 1:
                return False
        return True

    def rotate(self, rotate_index):
        self.ops.append(rotate_index)
        if rotate_index == 1:
            self.board[0], self.board[1], self.board[4], self.board[3] = \
                self.board[3], self.board[0], self.board[1], self.board[4]
        elif rotate_index == 2:
            self.board[3], self.board[4], self.board[7], self.board[6] = \
                self.board[6], self.board[3], self.board[4], self.board[7]
        elif rotate_index == 3:
            self.board[6], self.board[7], self.board[9], self.board[10] = \
                self.board[10], self.board[6], self.board[7], self.board[9]
        elif rotate_index == 4:
            self.board[1], self.board[2], self.board[4], self.board[5] = \
                self.board[5], self.board[1], self.board[2], self.board[4]
        elif rotate_index == 5:
            self.board[4], self.board[5], self.board[7], self.board[8] = \
                self.board[8], self.board[4], self.board[5], self.board[7]
        elif rotate_index == 6:
            self.board[7], self.board[8], self.board[10], self.board[11] = \
                self.board[11], self.board[7], self.board[8], self.board[10]
