import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
from func_search import SearchOnline

class SearchFacebook(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(SearchFacebook, self).__init__(*args, **kwargs)
        self.title = "Kiểm tra website thương mại điện tử"
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
        font = QFont()

        #menu tool box
        #label
        self.label = QLabel(self)
        self.label.move(125, 14)
        self.label.resize(400,25)
        self.label.setFont(QFont("Segoe UI Semibold", 14))
        self.label.setText("KIỂM TRA WEBSITE THƯƠNG MẠI ĐIỆN TỬ")

        #textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(80, 50)
        self.textbox.resize(390, 27)
        self.textbox.setFont(QFont("Segoe UI Semibold", 10))

        #button
        self.button = QPushButton('Kiểm tra', self)
        self.button.setToolTip('Start Searching...')
        self.button.move(480, 50)
        self.button.resize(80, 27)
        self.button.setFont(QFont("Segoe UI Semibold", 10))
        self.button.clicked.connect(self.on_click_button)

        #textarea
        self.textarea = QTextEdit(self)
        self.textarea.move(80, 90)
        self.textarea.resize(480, 200)
        self.textarea.setFont(QFont("Segoe UI Semibold", 10))
        self.show()

    def on_click_button(self):
        textboxValue = self.textbox.text()
        if textboxValue == "":
            self.textarea.setText("Bạn chưa nhập gì cả!!!")
        else:
            self.Search = SearchOnline(textboxValue)
            self.textarea.setText(self.Search.search())
            self.textbox.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = SearchFacebook()
    sys.exit(app.exec_())
