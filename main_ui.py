# -*- coding: utf8 -*-

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow

from board import Board
from simulator import Simulator


class ResolverUI(QMainWindow):
    message_signal = QtCore.pyqtSignal(str)

    def __init__(self):
        super(ResolverUI, self).__init__()
        self.setWindowTitle("XXLFR")
        self.setWindowIcon(QIcon("./res/logo.png"))
        self.setFixedSize(600, 700)
        self.setFont(QtGui.QFont("Sans", 13))

        self.widget = QtWidgets.QWidget()
        self.setCentralWidget(self.widget)

        self.main_h_layout = QtWidgets.QHBoxLayout(self.widget)
        self.spacer_l = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.main_v_layout = QtWidgets.QVBoxLayout(self.widget)
        self.spacer_r = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.main_h_layout.addItem(self.spacer_l)
        self.main_h_layout.addLayout(self.main_v_layout)
        self.main_h_layout.addItem(self.spacer_r)

        self.spacer_t = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.content_layout = QtWidgets.QHBoxLayout()
        self.run_button = QtWidgets.QPushButton("Run")
        self.run_button.setMinimumHeight(50)
        self.result = QtWidgets.QTextEdit()
        self.result.setEnabled(False)
        self.result.setFont(QtGui.QFont("Sans", 15))
        self.spacer_b = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.main_v_layout.addItem(self.spacer_t)
        self.main_v_layout.addLayout(self.content_layout)
        self.main_v_layout.addWidget(self.run_button)
        self.main_v_layout.addWidget(self.result)
        self.main_v_layout.addItem(self.spacer_b)

        self.left_button_layout = QtWidgets.QVBoxLayout()
        self.board_layout = QtWidgets.QGridLayout()
        self.right_button_layout = QtWidgets.QVBoxLayout()
        self.content_layout.addLayout(self.left_button_layout)
        self.content_layout.addLayout(self.board_layout)
        self.content_layout.addLayout(self.right_button_layout)

        self.button_group = QtWidgets.QButtonGroup()
        self.buttons = [QtWidgets.QPushButton() for _ in range(6)]
        for i in range(3):
            self.left_button_layout.addWidget(self.buttons[i])
            self.right_button_layout.addWidget(self.buttons[i + 3])

        for i in range(6):
            self.buttons[i].setText(str(i + 1))
            self.buttons[i].setFixedSize(60, 60)
            self.button_group.addButton(self.buttons[i], i + 1)

        self.texts = [QtWidgets.QLineEdit() for _ in range(12)]
        for i in range(4):
            for j in range(3):
                index = i * 3 + j
                self.texts[index].setText(str(index + 1))
                self.texts[index].setFixedSize(80, 80)
                self.texts[index].setAlignment(QtCore.Qt.AlignCenter)
                self.board_layout.addWidget(self.texts[index], i, j)

        self.run_button.clicked.connect(self.run)
        self.button_group.buttonClicked[int].connect(self.rotate)
        self.message_signal.connect(self.update_result)

    def run(self):
        board = [int(self.texts[i].text()) for i in range(12)]
        simulator = Simulator(board, self.message_signal)
        self.result.setText("Simulating")
        QtCore.QThreadPool.globalInstance().start(simulator)

    def rotate(self, rotate_index):
        board = Board([int(self.texts[i].text()) for i in range(12)])
        board.rotate(rotate_index)
        for i in range(12):
            self.texts[i].setText(str(board.board[i]))

    def update_result(self, message):
        self.result.setText(message)
