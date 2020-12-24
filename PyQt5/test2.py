import argparse
import sys
from random import randint
from time import sleep, time
import os

#khai báo thư viện cho selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


#khai báo thư viện cho bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup

link = "http://online.gov.vn/searchProfile/Index?KeySearch={}&btnRadioSearch=opt-domain-web-name-app"

class SearchOnline:
    def __init__(self, keyword):
        super(SearchOnline, self)
        self.keyword = keyword
        options = webdriver.ChromeOptions()
        #options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path=r'C:\\gitclone\\python\\chromedriver.exe', options=options)

    def get_info_of_detail(self):
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

        flag = 1
        result = ""
        result = result + "----------------------------------------------" + "\n" + str(self.driver.current_url) + "\n"
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
        return result


    def search(self):
        result = []
        self.driver.get(link.format(self.keyword))
        links = [url.get_attribute("href") for url in self.driver.find_elements(By.LINK_TEXT, "Xem chi tiết")]
        for url in links:
            self.driver.get(url)
            self.get_info_of_detail()
            result.append(self.get_info_of_detail())
        print (result)

        
if __name__ == "__main__":
    keyinput = "batdongsan"
    Search = SearchOnline(keyinput)
    Search.search()
