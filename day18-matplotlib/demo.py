import matplotlib.pyplot as plt

squares = [1,4,9,16,25]

#python 3.8 有些属性不存在
plt.plot(squares)
#设置图标标题，并给坐标轴加上标签
plt.title("Square Numbers",fontdict=24)
plt.xlabel("value",fontdict=24)
plt.ylabel("Square of value",fontdict=24)

#设置刻度标记的大小
plt.tick_params(axis='both',labelsize=14)
plt.show()

