import matplotlib.pyplot as plt



# ------------------example 1---------------
# squares = [1,4,9,16,25]
# # linewidth 设置曲线线条的粗细
# plt.plot(squares,linewidth=5)
# plt.title("Square Numbers",fontsize = 24)
# plt.xlabel("Value",fontsize=24)
# plt.ylabel("Square of Value",fontsize=24)
# # 设置刻度标记的大小
# plt.tick_params(axis='both',labelsize=14)
# plt.savefig('example1.png', bbox_inches = 'tight')
# plt.show()


# -----------------example 2----------------
# input_values = [1,2,3,4,5]
# squares = [1,4,9,16,26]
# plt.plot(input_values,squares,linewidth=5)
# plt.title("Square Numbers",fontsize = 24)
# plt.xlabel("Value",fontsize=24)
# plt.ylabel("Square of Value",fontsize=24)
# # 设置刻度标记的大小
# plt.tick_params(axis='both',labelsize=14)
# plt.savefig('example2.png', bbox_inches = 'tight')
# plt.show()



# -----------------example 3----------------
# # plt.scatter(2,4,s=200)
# # plt.show()
# x_values = [1,2,3,4,5]
# y_values = [1,4,9,16,25]
# plt.scatter(x_values,y_values,s=100)
# plt.savefig('example3.png', bbox_inches = 'tight')
# plt.show()

# -----------------example 4----------------
# 自动计算数据
# x_values = list(range(1,1001))
# y_values = [x**2 for x in x_values]
# # 删除数据点的轮廓 edgecolors = 'none'
# plt.scatter(x_values,y_values,s=4,edgecolors='none',c=(0,0,0.8))
# # 给x轴和y轴新增标签范围 函数axis提供了4个参数
# plt.axis([0,1100,0,1100000])
# plt.savefig('example4.png', bbox_inches = 'tight')
# plt.show()

# -----------------example 5---------------
# 颜色映射 起始颜色渐变到结束颜色 由浅入深
x_values = list(range(1001))
y_values = [x**2 for x in x_values]
# 虚线的范围由浅入深 参数c设置成一个列表
# cmap使用哪个颜色映射
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolors="none",s=40)
# bbox_inches  指定将图表多余的空白区域裁减掉。
# savefig保存图片
plt.savefig('example5.png', bbox_inches = 'tight')
plt.show()

