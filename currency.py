import sys
import json
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QComboBox, QLabel, QHBoxLayout
from PyQt6 import QtGui

class DisplayWindow(QMainWindow):

    def __init__(self, parent = None):
        super().__init__(parent)

        # Initialize file path
        file_path = "./currencies.json"

        # Open the file and load its contents into a list
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        currency_names = [currency["name"] for currency in data.values()]

        print(data)
        
        self.setWindowTitle("Currency converter")
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setGeometry(100, 100, 400, 200)

        # Create a central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Set up a vertical layout for the main window
        main_layout = QVBoxLayout(central_widget)

        # Create a horizontal layout for the dropdowns
        dropdown_layout = QHBoxLayout()

        # Create a vertical layout for the first dropdown
        first_dropdown_layout = QVBoxLayout()
        self.combo1 = QComboBox()
        self.combo1.addItems(currency_names)
        first_dropdown_layout.addWidget(QLabel("Select from Dropdown 1:"))
        first_dropdown_layout.addWidget(self.combo1)

        # Create a vertical layout for the second dropdown
        second_dropdown_layout = QVBoxLayout()
        self.combo2 = QComboBox()
        self.combo2.addItems(currency_names)
        second_dropdown_layout.addWidget(QLabel("Select from Dropdown 2:"))
        second_dropdown_layout.addWidget(self.combo2)

        # Add the vertical layouts to the horizontal layout
        dropdown_layout.addLayout(first_dropdown_layout)
        dropdown_layout.addLayout(second_dropdown_layout)

        # Add the horizontal layout to the main layout
        main_layout.addLayout(dropdown_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = DisplayWindow()
    win.show()
    sys.exit(app.exec())