import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.linspace(-1,1,50)
y2 = x*2+1
y = x**2
plt.figure(figsize=(4,4))
#color设置实线的颜色，linewidth设置实线的宽度 linestyle设置曲线样式

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

#图例制作  label 设置图例名称
l1,= plt.plot(x,y2,label='up')
l2,= plt.plot(x,y,color="red",linewidth=1.0,linestyle='--',label='down')
#设置名称以及图例所在位置
plt.legend(handles=[l1,l2,],labels=['aaa','bbb'],loc='best')
plt.show()