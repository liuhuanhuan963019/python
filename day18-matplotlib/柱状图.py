import numpy as np
import matplotlib.pyplot as plt

n=12  #表示12个向上或者12个向下的柱状图
X = np.arange(n) #生成0-11的数组

Y1 = (1-X/float(n))*np.random.uniform(0.5,1.0,n)  #产生0.5-1范围内的数值
Y2 = (1-X/float(n))*np.random.uniform(0.5,1.0,n)


#设置图形的颜色和背景颜色
plt.bar(X,+Y1,facecolor='#9999ff',edgecolor='white')
plt.bar(X,-Y2,facecolor='#ff9999',edgecolor='white')

for x,y in zip(X,Y1):
    plt.text(x+0.4,y+0.05,'%.2f' % y,ha='center',va='bottom')

for x,y in zip(X,Y2):
    plt.text(x+0.4,-y-0.05,'%.2f' % y,ha='center',va='bottom')

plt.show()

