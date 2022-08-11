import pandas as pd
path = 'E:/pandas/课件011/计算日期.xlsx'
data = pd.read_excel(path,index_col='序号')
print(data)
print('==========================')
data['间隔'] = data['结束日期']-data['起始日期']
print(data)