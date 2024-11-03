import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import QtGui

class DisplayWindow(QMainWindow):

    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.setWindowTitle("Currency converter")
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.resize(500,400)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = DisplayWindow()
    win.show()
    sys.exit(app.exec())