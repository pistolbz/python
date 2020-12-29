import argparse
import sys
from random import randint
from time import sleep, time
import time
import os
os.chdir("C:\\gitclone\\python\\PyQt5\\")
#khai báo thư viện cho selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#khai báo thư viện cho bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup

link = "http://online.gov.vn/searchProfile/Index?KeySearch={}&btnRadioSearch=opt-domain-web-name-app"
file = open("details.txt", "w", encoding="utf-8")
class SearchOnline:
    def __init__(self, keyword):
        super(SearchOnline, self)
        self.keyword = keyword
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path=r'C:\\gitclone\\python\\chromedriver.exe', options=options)

    def check_logo(self):
        check = self.driver.find_element_by_class_name("imageGridDetailLogo").get_attribute("src")
        check_result = "Tình trạng đăng ký: \n"
        if (str(check) == 'http://online.gov.vn/Content/EndUser/LogoCCDVSaleNoti/logoSaleNoti.png'):
            check_result = check_result + "Đã thông báo"
        else:
            if (str(check) == 'http://online.gov.vn/Content/EndUser/LogoCCDVSaleNoti/logoCCDV.png'):
                check_result = check_result + "Đã đăng ký"
            else:
                check_result = check_result + "Website chưa được xác nhận"
        return check_result
 

    def get_info_of_detail(self):
        detail = ""
        info = self.driver.find_elements_by_class_name("col-xs-6")
        for tt in info:
            detail += tt.text + "\n"
        return detail

    def search(self):
        start_time = time.time()
        result = ""
        self.driver.get(link.format(self.keyword))
        onclick = "a[onclick^='GetSearchResultWeb({})']"
        i = 1
        links = []
        while True:
            try:
                for url in self.driver.find_elements(By.LINK_TEXT, "Xem chi tiết"):
                    links.append(str(url.get_attribute("href")))
            except:
                pass
            try:
                i += 1
                page = self.driver.find_element_by_css_selector(onclick.format(i))
                page.click()
            except:
                break
            
        for url in links:
            print(url)
            self.driver.get(url)
            result += self.get_info_of_detail() + self.check_logo() + "\n\n"
        self.driver.close()
        file.write(result)
        time_exec = time.time() - start_time
        result = "Chúng tôi tìm thấy " + str(len(links)) + " kết quả!!\nChương trình thực thi trong " + str(time_exec) + "s\n" + result
        return result


        
if __name__ == "__main__":
    keyinput = "batdongsan.vn"
    Search = SearchOnline(keyinput)
    Search.search()
