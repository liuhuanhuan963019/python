import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3,3,50)

y = 0.1 * x

plt.figure()
plt.plot(x,y,color='b',linewidth=10)
plt.ylim(-2,2)

#设置周围点
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

#设置底部透明度，样式
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor='white',edgecolor='None',alpha=0.7))

plt.show()