# 3.2.1 多个字典序列创建DataFrame
import pandas as pd
dict = {
'姓名':['孙兴华','李小龙','叶问'],
'年龄':[20,80,127],
'功夫':['撸铁','截拳道','咏春']
}
data = pd.DataFrame(dict)
print(data)

print()
print()

# 如果只查询一列，返回的是pd.Series
print(data['姓名'])
print()
# 指定行查询
print(data.loc[1])
print()
# 指定行列查询
print(data.loc[1]['姓名'])
print()


# 如果查询多列，返回的是pd.DataFrame
print(data[['姓名','年龄']]) # 返回索引和这两列数据
print()

# • 如果查询多行，返回的是pd.DataFrame
print(data.loc[1:3]) # 返回前3行，包括结束值
print()

# 将多个Series加入DataFrame
import pandas as pd
data1 = pd.Series(['叶问','李小龙','孙兴华'],index=[1,2,3],name='姓名')
data2 = pd.Series(['男','男','男'],index=[1,2,3],name='性别')
data3 = pd.Series([127,80,20],index=[1,2,3],name='年龄')

table = pd.DataFrame({data1.name: data1, data2.name: data2, data3.name: data3})
print(table)
