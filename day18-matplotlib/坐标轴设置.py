import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(-1,1,50)
y = x**2
plt.figure(figsize=(10,10))
#color设置实线的颜色，linewidth设置实线的宽度 linestyle设置曲线样式
plt.plot(x,y,color="red",linewidth=1.0,linestyle='--')

#设置坐标轴范围
plt.xlim(-1,2)
plt.ylim(-2,3)
#设置坐标轴名称
plt.xlabel("i am x")
plt.ylabel("i am y")

#设置坐标间隔范围
new_ticks = np.linspace(-1,2,5)
print(new_ticks)
plt.xticks(new_ticks)
#设置对应y轴名称
#通过使用r'$ $'方式可以使得坐标轴文字相对美观
plt.yticks([-2,-1.8,-1,1.22,2],
           [r'$really\ bad$',r'$bad\ \alpha$',r'$normal$',r'$good$',r'$really\ good$'])

#gca = 'get current axis' 获取当前坐标轴的
ax = plt.gca()
#设置顶部与右侧的边框为none
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

#设置指定的x轴与y轴
#设置底部为x轴
ax.xaxis.set_ticks_position('bottom')
#设置左侧为y轴
ax.yaxis.set_ticks_position('left')

#修改坐标轴顺序
#表示横坐标的值是纵坐标的0
ax.spines['bottom'].set_position(("data",0))
#表示纵坐标的值是横坐标的0
ax.spines['left'].set_position(("data",0))









plt.show()
