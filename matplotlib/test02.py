import pandas as pd
import matplotlib.pyplot as plt

# 水平柱状图，基于test01

# 数据中有中文，设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
# 解决坐标轴负号问题
# plt.rcParams['axes.unicode_minus'] = False
# 读取Excel文件
data = pd.read_excel("01.柱状图.xlsx")
# 对数据进行排序
data.sort_values(by="分数",inplace=True,ascending=False)
# 画柱状图
plt.bar(x=0,bottom=data.姓名,height=0.5,width=data.分数,orientation="horizontal",color="red",alpha=0.5)

# x，y轴的标题
plt.xlabel("姓名")
plt.ylabel("分数")
# 刻度标签以及文字旋转的角度
# plt.xticks(data.姓名,rotation=90)
# y轴的刻度范围
# plt.ylim([0,100])

# plt.tight_layout()
# 图表标题
plt.title("三年级二班学生成绩",fontsize=16)
# 保存位置
plt.savefig(r"d:\柱状图.jpg")

plt.show()