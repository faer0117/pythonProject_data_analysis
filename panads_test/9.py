import pandas as pd
import datetime as dt

path = ('E:/pandas/课件010/自动填充.xlsx')
start_date = dt.date(2020,1,1)
data = pd.read_excel(path,skiprows=0,usecols="A:D",index_col=None,dtype={'序号':str,'性别':str,'日期':str})

for i in data.index:
    data.at[i,'序号'] = i + 1
    data.at[i,'性别'] = '男' if i%2 == 0 else '女'
    data.at[i,'日期'] = start_date

data.set_index('序号',inplace=True)
print(data)
data.to_excel(path)