import pandas as pd
path = 'E:/pandas/课件011/apply函数.xlsx'
data = pd.read_excel(path,index_col='序号')
print(data)
print("============================================")


data['加分']=data['民族'].apply(lambda x:5 if x != '汉' else 0)
data['最终分数'] = data['总分']+data['加分']

print(data)