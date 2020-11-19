import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,10,0.1)
y1 = 0.05 * x ** 2
y2 = -1 * y1

fig,ax1 = plt.subplots()
# ax1.spines["right"].set_color('none')
# ax1.spines["top"].set_color('none')

ax2 = ax1.twinx()
ax1.plot(x,y1,'g-')
ax2.plot(x,y2,'b--')

ax1.set_xlabel('X data')
ax1.set_ylabel('Y1',color='g')
ax1.set_ylabel('Y2',color='b')
plt.show()