import numpy as np
# 使用ones创建全是1的数组
a = np.ones(3,dtype=int)
a2 = np.ones((2,3),dtype=int)

print(a)
print(a2)
# zeros 创建全是0的数组

b = np.zeros(3,dtype=int)
b2 = np.zeros((2,3),dtype=int)

print(b)
print(b2)

# full创建指定值的数组

c = np.full((2,3),5)
print(c)

# 使用random模块生成随机数组
aa = np.random.randn() # 一个随机数
bb = np.random.randn(3) # 3个数
cc = np.random.randn(3,2) # 3行2列
dd = np.random.randn(3,2,4) # 3块，每块是2行4列

print("==========")
print(aa)
print(bb)
print(cc)
print(dd)