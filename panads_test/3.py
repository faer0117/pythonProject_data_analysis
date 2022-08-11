import pandas as pd
import xlrd
import openpyxl

# txt文件转csv文件
path = 'E:/pandas/课件001-005/读取文件.txt'

data = pd.read_csv(path)

data.to_csv('E:/pandas/111.csv')

print("转换成功")