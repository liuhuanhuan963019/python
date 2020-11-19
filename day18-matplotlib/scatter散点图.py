import numpy as np
import matplotlib.pyplot as plt


n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
T= np.arctan2(Y,X)  #for color 颜色渲染

plt.scatter(X,Y,s=75,c=T,alpha=0.5)

#设置x,y的坐标范围
plt.xlim(-1.5,1.5)
plt.ylim(-1.5,1.5)
#设置刻度为none
plt.xticks(())
plt.yticks(())
plt.show()
