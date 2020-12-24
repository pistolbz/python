import argparse
import sys
from random import randint
from time import sleep

from selenium import webdriver  #sửa lỗi không chạy đc firefox bằng cách thêm grocdriver vào scripts trong Python
from selenium.webdriver.chrome.options import Options

linksearch = "http://online.gov.vn/"
class SearchOnline:
    def __init__(self, keyword):     #nhằm tạo self usr và pwd
        self.keyword = keyword
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        #options.add_argument("user-data-dir=C:\\Users\\Admin\\AppData\\Local\\Google\\Chrome\\User Data")
        self.driver = webdriver.Chrome(executable_path=r'C:\\gitclone\\python\\chromedriver.exe', options=options)

    def search(self):
        self.driver.get(linksearch)
        keyword_ele = self.driver.find_element_by_css_selector('#searchInputOpt')
        keyword_ele.send_keys(self.keyword)
        login_ele = self.driver.find_element_by_css_selector('body > div.BgWhite > div.container.main-gov > div > div.col-sm-8.col-8-gov > div.tra-cuu-dek-onlinegov > form > div:nth-child(1) > div.tra-cuu-right.hide-on-mobile > div > button')
        login_ele.click()
    
    def check(self):
        xemchitiet_ele = self.driver.find_element_by_css_selector('#tableWeb > tbody > tr > td:nth-child(4) > a')
        xemchitiet_ele.click()
        img = self.driver.find_element_by_css_selector('#containerBOX.container.BgWhite > div.col-sm-8 > div.row > div.col-sm-12 > div.row.boxDetailDataDisplay > div.text-center.col-xs-12 > img.imageGridDetailLogo')
        src = img.get_attribute("src")
        #print(src)
        if(src == 'http://online.gov.vn/Content/EndUser/LogoCCDVSaleNoti/logoCCDV.png'):
            print("Đã đăng ký")
        else:
            if(src == 'http://online.gov.vn/Content/EndUser/LogoCCDVSaleNoti/logoSaleNoti.png'):
                print("Đã thông báo")
            else:
                print("Đang tiến hành kiểm tra")
        

    def result(self):
        try:
            self.driver.find_element_by_css_selector('#tableWeb > tbody > tr > td:nth-child(4) > a')
            return True
        except:
            return False


    
if __name__ == '__main__':
    
    keyinput = "shopee.vn"
    Search = SearchOnline(keyinput)

    Search.search()
    if Search.result():
        Search.check()
    else:
        print("ohh")

