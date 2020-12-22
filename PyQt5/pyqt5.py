import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(App, self).__init__(*args, **kwargs)
        self.title = "Learn PyQt5 the hard way"
        self.left = 10
        self.top = 10
        self.width = 420
        self.height = 320
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        #menubar
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')
        viewMenu = mainMenu.addMenu('View')
        helpMenu = mainMenu.addMenu('Help')

        #button of menubar
        exitButton = QAction(QIcon(), "Exit", self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)

        #textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(40, 40)
        self.textbox.resize(280, 22)

        #button
        self.button = QPushButton('Click', self)
        self.button.setToolTip('This is example button')
        self.button.move(324, 40)
        self.button.resize(50, 22)
        self.button.clicked.connect(self.on_click_button)

        #table
        #self.createTable()
        #self.layout = QVBoxLayout()
        #self.layout.addWidget(self.tableWidget)
        #self.setLayout(self.layout)

        self.show()

    def createTable(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setItem(0, 0, QTableWidgetItem("Cell (1,1)"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("Cell (1,2)"))
        self.tableWidget.setItem(1, 0, QTableWidgetItem("Cell (2,1)"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("Cell (2,2)"))
        self.tableWidget.setItem(2, 0, QTableWidgetItem("Cell (3,1)"))
        self.tableWidget.setItem(2, 1, QTableWidgetItem("Cell (3,2)"))
        self.tableWidget.setItem(3, 0, QTableWidgetItem("Cell (4,1)"))
        self.tableWidget.setItem(3, 1, QTableWidgetItem("Cell (4,2)"))
        self.tableWidget.move(40, 80)

        self.tableWidget.doubleClicked.connect(self.on_click_table)

    @pyqtSlot()
    def on_click_table(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())


    @pyqtSlot()
    def on_click_button(self):
        textboxValue = self.textbox.text()
        if textboxValue != "":
            message = "You typed: " + textboxValue    
        else:
            message = "We don't have anything on textbox!"
        QMessageBox.question(self, 'Message', message, QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

