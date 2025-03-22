from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QLineEdit, QLabel
import sys
from PyQt5.QtGui import QIcon, QFont, QColor

class App(QWidget):
    def __init__(self):
        super().__init__()
        # window = QMainWindow()
        self.setStyleSheet('background-color: #CBCAC5;')
        self.title= "Catahan - Laboratory Activity #9"
        self.x=200
        self.y=200
        self.width=500
        self.height=600
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y, self.width, self.height)
        self.setWindowIcon (QIcon('angel-wings_38475.ico'))
        self.textboxlbl = QLabel("Account Registration System", self)
        self.textboxlbl.move(80,20)
        self.textboxlbl.setFont(QFont('Times New Roman', 20, QFont.Bold))


        # Create textbox

        self.textboxlbl1 = QLabel("Enter your first name:", self)
        self.textboxlbl1.move(20,86)
        self.textboxlbl1.setFont(QFont('Times New Roman', 11))
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(180, 80)
        self.textbox1.resize(295,30)
        self.textbox1.setText('')
        self.textbox1.setStyleSheet('background-color: White;')

        self.textboxlbl2 = QLabel("Enter your last name:", self)
        self.textboxlbl2.move(20,155)
        self.textboxlbl2.setFont(QFont('Times New Roman', 11))
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(180, 150)
        self.textbox2.resize(295,30)
        self.textbox2.setText('')
        self.textbox2.setStyleSheet('background-color: White;')

        self.textboxlbl3 = QLabel("Enter your username:", self)
        self.textboxlbl3.move(20,225)
        self.textboxlbl3.setFont(QFont('Times New Roman', 11))
        self.textbox3 = QLineEdit(self)
        self.textbox3.move(180, 220)
        self.textbox3.resize(295,30)
        self.textbox3.setText('')
        self.textbox3.setStyleSheet('background-color: White;')

        self.textboxlbl4 = QLabel("Enter your password:", self)
        self.textboxlbl4.move(20,294)
        self.textboxlbl4.setFont(QFont('Times New Roman', 11))
        self.textbox4 = QLineEdit(self)
        self.textbox4.move(180, 290)
        self.textbox4.resize(295,30)
        self.textbox4.setText('')
        self.textbox4.setStyleSheet('background-color: White;')

        self.textboxlbl5 = QLabel("Enter your own email:", self)
        self.textboxlbl5.move(20,366)
        self.textboxlbl5.setFont(QFont('Times New Roman', 11))
        self.textbox5 = QLineEdit(self)
        self.textbox5.move(180, 360)
        self.textbox5.resize(295,30)
        self.textbox5.setText('')
        self.textbox5.setStyleSheet('background-color: White;')


        self.textboxlbl6 = QLabel("Enter your contact #:", self)
        self.textboxlbl6.move(20,435)
        self.textboxlbl6.setFont(QFont('Times New Roman', 11))
        self.textbox6 = QLineEdit(self)
        self.textbox6.move(180, 430)
        self.textbox6.resize(295,30)
        self.textbox6.setText('')
        self.textbox6.setStyleSheet('background-color: White;')


        #SUBMIT
        self.button = QPushButton('SUBMIT', self)
        self.button.setToolTip("Are you sure you want to submit?")
        self.button.move(100,500) # button.move(x,y)
        self.button.resize(100, 50)
        self.button.setStyleSheet('background-color: #E1EEC9;')
        self.button.setFont(QFont('Times New Roman', 12))
        #CLEAR
        self.button2 = QPushButton('CLEAR', self)
        self.button2.setToolTip("Are you sure you want to clear?")
        self.button2.move(300, 500)  # button.move(x,y)
        self.button2.resize(100, 50)
        self.button2.setStyleSheet('background-color: #EED0C9;')
        self.button2.setFont(QFont('Times New Roman', 12))
        self.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App() #exec: exec
    sys.exit(app.exec_())