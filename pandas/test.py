import pandas as pd
import openpyxl
import xlwt
import os
os.chdir("C:\\gitclone\\python\\pandas\\")

path = 'details.xlsx'

data = pd.DataFrame([['shopee.vn','','Sàn giao dịch TMĐT, Website khuyến mại trực tuyến','Công ty TNHH Shopee','0106773786','Tầng 28, Tòa nhà trung tâm Lotte Hà Nội, số 54 đường Liễu Giai, P.Cống Vị, Q.Ba Đình, Tp. Hà Nội','Hà Nội','Việt Nam','02473081221']])

with pd.ExcelWriter(path, mode='a') as writer:
    writer.book = openpyxl.load_workbook(path)
    data.to_excel(writer)
