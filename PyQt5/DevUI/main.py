import sys, os
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
from func_search import SearchOnline

os.chdir("C:\\gitclone\\python\\PyQt5\\DevUI\\")

class SearchFacebook:
    def __init__(self, *args, **kwargs):
        super(SearchFacebook, self).__init__(*args, **kwargs)
        self.window = uic.loadUi("main.ui")
        self.window.setWindowTitle("CHƯƠNG TRÌNH KIỂM TRA WEBSITE THƯƠNG MẠI ĐIỆN TỬ")
        self.initUI()
    
    def initUI(self):
        #set init
        self.lbMain = self.window.lbMain
        self.txtSearch = self.window.txtSearch
        self.btnSearch = self.window.btnSearch
        self.txtResult = self.window.txtResult
        self.sttBar = self.window.sttBar

        #button
        self.btnSearch.clicked.connect(self.on_click_btnSearch)

        #show
        self.window.show()

    def on_click_btnSearch(self):
        txtSearch = self.txtSearch.text()
        if txtSearch == "":
            self.txtResult.setText("Bạn chưa nhập gì cả!!!")
        else:
            self.Search = SearchOnline(txtSearch)
            self.txtResult.setText(self.Search.search())
            self.txtSearch.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = SearchFacebook()
    sys.exit(app.exec_())