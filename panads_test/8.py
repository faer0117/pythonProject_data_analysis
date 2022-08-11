# MultipleKey Merge (基于多个key上的merge)
import pandas as pd
data1 = pd.DataFrame({'姓名': ['张三', '张三', '王五'],'班级': ['1班', '2班', '1班'],'分数': [10,20,30]})
#    姓名  班级  分数
# 0  张三  1班  10
# 1  张三  2班  20
# 2  王五  1班  30
# print(data1)
data2 = pd.DataFrame({'姓名': ['张三', '张三', '王五','王五'],'班级': ['1班', '1班', '1班','2班'],'分数': [40,50,60,70]})
# print(data2)
#    姓名  班级  分数
# 0  张三  1班  40
# 1  张三  1班  50
# 2  王五  1班  60
# 3  王五  2班  70


# 内连接（交集）的结果
data3 = pd.merge(data1,data2,on=['姓名','班级'])
print(data3)
print()

# 外连接（并集）的结果
data4  = pd.merge(data1,data2,on = ['姓名','班级'],how='outer')
print(data4)
print()


data5 = pd.merge(data1,data2,on='姓名')
print(data5)