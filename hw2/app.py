from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QAction
import os
import sys
from functools import partial
import signal

from problems import problem1
from problems import problem2
from problems import problem3

class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainUi, self).__init__()
        ui_path = os.getcwd() + os.sep + "ui" + os.sep + "hw2.ui"
        uic.loadUi(ui_path, self)
        self.img_dir = os.getcwd() + os.sep + "images" + os.sep
        self._bind_buttons()
        problem3.init(self)

        self.show()

    def _bind_buttons(self):
        bind_dict = {
            'b1_1': problem1.p1_1,
            'b2_1': problem2.p2_1,
            'b3_1': problem3.p3_1,
            'b3_2': problem3.p3_2,
        }
        for object_name, bind_function in bind_dict.items():
            self.findChild(QtWidgets.QPushButton, object_name).clicked.connect(partial(bind_function, self))

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal.SIG_DFL) # Trap the Ctrl-C and terminate
    app = QtWidgets.QApplication(sys.argv)
    window = MainUi()
    sys.exit(app.exec_())