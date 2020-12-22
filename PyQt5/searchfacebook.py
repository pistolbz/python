import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont

class SearchFacebook(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(SearchFacebook, self).__init__(*args, **kwargs)
        self.title = "Search Facebook"
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 320
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        #center of app
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        #menu tool box
        #textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(80, 50)
        self.textbox.resize(390, 27)

        #button
        self.button = QPushButton('Search', self)
        self.button.setToolTip('Start Searching...')
        self.button.move(480, 50)
        self.button.resize(80, 27)
        self.button.clicked.connect(self.on_click_button)

        #textarea
        self.textarea = QTextEdit(self)
        self.textarea.move(80, 90)
        self.textarea.resize(480, 200)

        self.show()

    def on_click_button(self):
        print("ok")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = SearchFacebook()
    sys.exit(app.exec_())
