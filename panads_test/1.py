import  pandas as pd
import xlrd
import openpyxl

# 写文件
path = 'E:/pandas/excel_test1.xlsx'

data = pd.DataFrame(
    {'id':[1,2,3],
     '姓名':['叶问','李小龙','孙兴华']}
)
data = data.set_index('id')

data.to_excel(path)

print("新建excel文件成功")