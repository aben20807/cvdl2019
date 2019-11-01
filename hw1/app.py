from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QAction
import os
import sys
from functools import partial
import signal

from problems import problem1
from problems import problem2
from problems import problem5

class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainUi, self).__init__()
        ui_path = os.getcwd() + os.sep + "ui" + os.sep + "hw1.ui"
        uic.loadUi(ui_path, self)
        self._bind_buttons()

        menubar = self.menuBar()
        close_all = QAction('Close all CV windows', self)
        close_all.triggered.connect(problem1.close_all)
        menubar.addAction(close_all)

        self.show()

    def _bind_buttons(self):
        bind_dict = {
            'b1_1': problem1.p1_1,
            'b1_2': problem1.p1_2,
            'b1_3': problem1.p1_3,
            'b1_4': problem1.p1_4,
            'b2_1': problem2.p2_1,
            'b5_1': problem5.p5_1,
            'b5_2': problem5.p5_2,
        }
        for object_name, bind_function in bind_dict.items():
            self.findChild(QtWidgets.QPushButton, object_name).clicked.connect(partial(bind_function, self))

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal.SIG_DFL) # Trap the Ctrl-C and terminate
    app = QtWidgets.QApplication(sys.argv)
    window = MainUi()
    sys.exit(app.exec_())