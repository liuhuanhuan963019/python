import matplotlib.pyplot as plt

#用scatter绘制散点图并设置其样式
plt.scatter(2,4)
# plt.show()

plt.scatter(2,3,s=200)

#设置标题并给坐标轴加上标签
plt.title("Square Numbers")
plt.xlabel("Value")
plt.ylabel("Square of value")

#设置刻度标记的大小
plt.tick_params(axis='both')
plt.show()


#使用scatter()绘制一系列的点
x_values = [1,2,3,4,5]
y_values = [1,4,9,16,25]
plt.scatter(x_values,y_values,s=100)
plt.show()




