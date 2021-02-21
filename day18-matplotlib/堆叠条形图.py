import matplotlib.pyplot as plt
import numpy as np

# 这两行代码解决 plt 中文显示的问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 输入统计数据
waters = ('碳酸饮料', '绿茶', '矿泉水', '果汁', '其他')
buy_number_male = [6, 7, 6, 1, 2]
buy_number_female = [9, 4, 4, 5, 6]

bar_width = 0.3  # 条形宽度
index_male = np.arange(len(waters))   # 男生条形图的横坐标
index_female = index_male + bar_width  # 女生条形图的横坐标

# 使用两次bar 函数画出两组条形图
plt.bar(index_male,height=buy_number_male,width=bar_width,color='b',label='男性')
plt.bar(index_female,height=buy_number_female,width=bar_width,color='g',label='女性')
# 显示图例
plt.legend()
plt.xticks(index_male + bar_width/2,waters)
plt.ylabel("购买量") #纵坐标轴标题
plt.title('购买饮用水情况的调查结果')  # 图形标题
plt.savefig("堆叠条形图",bbox_inches='tight')
plt.show()