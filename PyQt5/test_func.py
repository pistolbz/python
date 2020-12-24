import argparse
import sys
from random import randint
from time import sleep, time
import os

#khai báo thư viện cho selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#khai báo thư viện cho bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup

class SearchOnline:
    def __init__(self, keyword):
        super(SearchOnline, self)
        self.keyword = keyword
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path=r'C:\\gitclone\\python\\chromedriver.exe', options=options)

    def search(self):
        result = ""
        self.driver.get("http://online.gov.vn/")
        keyword_ele = self.driver.find_element_by_css_selector('#searchInputOpt')
        keyword_ele.send_keys(self.keyword)
        self.driver.find_element_by_css_selector('body > div.BgWhite > div.container.main-gov > div > div.col-sm-8.col-8-gov > div.tra-cuu-dek-onlinegov > form > div:nth-child(1) > div.tra-cuu-right.hide-on-mobile > div > button').click()
        data = []

        

        #[data.append(st.get_attribute("href")) for st in self.driver.find_elements_by_link_text("Xem chi tiết")]
        print(data)
        info = self.driver.find_element_by_class_name("col-sm-12 ").text
        check = self.driver.find_element_by_class_name("imageGridDetailLogo").get_attribute("src")
        check_result = "Tình trạng đăng ký: \n"
        if (str(check) == 'http://online.gov.vn/Content/EndUser/LogoCCDVSaleNoti/logoSaleNoti.png'):
            check_result = check_result + "Đã thông báo"
        else:
            if (str(check) == 'http://online.gov.vn/Content/EndUser/LogoCCDVSaleNoti/logoCCDV.png'):
                check_result = check_result + "Đã đăng ký"
            else:
                check_result = check_result + "Website chưa được xác nhận"
        info = info + "\n" + check_result
        info = "Website không hợp lệ hoặc đây không phải là website thương mại điện tử!"


        flag = 1
        result = result + "-----------------------------------------------------------" + "\n" + str(self.driver.current_url) + "\n"
        for i in range(len(info)):
            if info[i] != "\n":
                result = result + info[i]
            else:
                if flag == 1:
                    result = result + "\n"
                    flag = 0
                else:
                    result = result + " "
                    flag = 1
        #print result

if __name__ == "__main__":
    keyinput = "batdongsan"
    Search = SearchOnline(keyinput)
    Search.search()
