# 比较数组与numpy多维对象

# 题目： 数组a与数组b相加，数组a是1~N数字的立方，数组b是1~N数字的平方
import numpy as np


def add(n):
    a=[i**3 for i in range(1,n+1)]
    print(a)
    b=[i**2 for i in range(1,n+1)]
    print(b)
    c = []
    for i in range(n):
        c.append(a[i]+b[i])
    return c

print(add(3))


# 使用numpy计算上面的题目
import numpy as np
def add2(n):
    a = np.arange(1,n+1)**3
    b = np.arange(1,n+1)**2
    return a+b

print(add2(3))