# 27MB
import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

from main_window_pyqt import Ui_MainWindow


class HelloWorldGui(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(HelloWorldGui, self).__init__(parent)
        self.setupUi(self)


class MyQApp(QApplication):
    def __init__(self, argvs):
        print('my init')
        if hasattr(sys, 'frozen'):
            print('library paths:', self.libraryPaths())
            try:
                self.removeLibraryPath('/opt/anaconda3/plugins')
                print('remove ok')
                print('library paths:', self.libraryPaths())
            except:
                pass
        print('orig init')
        super().__init__(argvs)
        # http://www.pyqtgraph.org/Bundling%20applications%20with%20PyQtGraph_R16.pdf


if __name__ == '__main__':
    argvs = sys.argv
    app = MyQApp(argvs)
    hello_world_gui = HelloWorldGui()
    hello_world_gui.show()
    sys.exit(app.exec_())
