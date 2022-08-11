import numpy as np
import pandas as pd
data1= pd.DataFrame({'姓名':['叶问','李小龙','孙兴华','李小龙','叶问','叶问'],'出手次数1':np.arange(6)})
data2 = pd.DataFrame({'姓名':['黄飞鸿','孙兴华','李小龙'],'出手次数2':[1,2,3]})
# 内连接
data3 = pd.merge(data1,data2,how='inner')
print(data3)
print()
# 左外连接
data3 = pd.merge(data1,data2,on='姓名',how='left')
print(data3)
print()
# 右外连接
data3 = pd.merge(data1,data2,on='姓名',how='right')
print(data3)

# 全连接
data3 = pd.merge(data1,data2,on='姓名',how='outer')
print()
print(data3)