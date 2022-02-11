# -*- coding: utf8 -*-

import sys

from PyQt5 import QtWidgets, QtCore

from main_ui import ResolverUI

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = ResolverUI()
    ui.show()
    sys.exit(app.exec())
