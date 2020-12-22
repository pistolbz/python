from urllib.request import urlopen
from bs4 import BeautifulSoup
from time import time
import os
t1 = time()
os.chdir("F:\\LEARN\\PYTHON\\Web scrapping\\")
file = open("online_validate/details.txt", "w", encoding="utf-8")
data = open("online_validate/list.txt", "w")
urlget = "http://online.gov.vn/Home/WebDetails/{}"
num = 1
start = 0
data.close()
for i in range(start + 1, start + 101):
    html = urlopen(urlget.format(i))
    res = BeautifulSoup(html.read(), "lxml")
    title = res.title.getText()
    if(title != "Không tìm thấy trang"):

        print(i)
        tags = res.findAll("div", {"class": "col-xs-6"})
        img = res.find("img", {"class": "imageGridDetailLogo"})
        file.write("\n\n--------------------------------\n" + str(num) + ". " + tags[2].getText().strip() + "\n--------------------------------\n")
        file.write(urlget.format(i) + "\n")
        num += 1
        a = 1
        for tag in tags:
            file.write(tag.getText().strip())
            a = (a + 1) % 2
            if(a != 1): 
                file.write("\n")
            else:
                file.write(" ")
        if (str(img) == '<img class="imageGridDetailLogo" src="/Content/EndUser/LogoCCDVSaleNoti/logoSaleNoti.png"/>'):
            file.write("Đã thông báo")
        else:
            if (str(img) == '<img class="imageGridDetailLogo" src="/Content/EndUser/LogoCCDVSaleNoti/logoCCDV.png"/>'):
                file.write("Đã đăng ký")
            else:
              file.write("Website chưa được xác nhận")

    res.decompose()
    html.close()

t2 = time()
elapsed = t2 - t1
print('Elapsed time is %f seconds.' % elapsed)