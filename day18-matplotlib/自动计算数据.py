import matplotlib.pyplot as plt

x_values = list(range(1,1001))

y_values = [x**2 for x in x_values]

#使用参数c传递颜色值，越接近0颜色越深
# plt.scatter(x_values,y_values,c='red',edgecolors='none',s=40)
# plt.scatter(x_values,y_values,c=(0,0,0.8),edgecolors='none',s=40)

#设置标题并给坐标轴加上标签
plt.title("Square Numbers")
plt.xlabel("Value")
plt.ylabel("Square of value")

#设置x,y 坐标轴的取值范围
plt.axis([0,1100,0,1100000])

#使用一些颜色映射  颜色渐变，从透明开始颜色变深
plt.scatter(x_values,y_values,c = y_values,cmap=plt.cm.Blues,
            edgecolors='none',s=40)

# pyplot所有的颜色映射，访问http://matplotlib.org/,单击Examples,向下滚动到
#colorExamples 再单击colormaps_reference

plt.savefig('square_plot.png',bbox_inches = 'tight')

# plt.show()