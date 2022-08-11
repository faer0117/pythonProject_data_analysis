import pandas
import pandas as pd
import xlrd
import openpyxl

# 读文件

# 读取Excel文件
path = 'E:/pandas/课件001-005/读取文件.xlsx'

data = pd.read_excel(path)
data.columns=['序号','姓名','年龄','地址','电话','入职日期']
data.set_index('序号',inplace=True)
print(data)
print("=====================")
# 读取前三行
print(data.head(3))
# 查看列名列表
print("=====================")
print(data.columns)

# 读取。txt文件
path = 'E:/pandas/课件001-005/读取文件.txt'

data = pd.read_table(path)

print("-------------------------------------------------------------------------------------------------------------------------------------")
print(data)

