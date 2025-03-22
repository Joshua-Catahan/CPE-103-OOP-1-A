from registration import App
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QLineEdit, QLabel
import sys
from PyQt5.QtGui import QIcon, QFont, QColor

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App() #exec: exec
    sys.exit(app.exec_())