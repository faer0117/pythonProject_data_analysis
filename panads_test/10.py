import pandas as pd
path = 'E:/pandas/课件011/计算列.xlsx'
data = pd.read_excel(path,index_col='序号')
print(data)
data['销售金额'] = data['单价']*data['销售数量']
print("=================================")
print(data)