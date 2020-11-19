import numpy as np
import matplotlib.pyplot as plt
from  mpl_toolkits.mplot3d import Axes3D


fig = plt.figure()  #定义图片的窗口
ax = Axes3D(fig)  #3D


#X,Y,value
X = np.arange(-4,4,0.25)
Y = np.arange(-4,4,0.25)

X,Y = np.meshgrid(X,Y)
R = np.sqrt(X ** 2 + Y ** 2)
Z = np.sin(R)

#plot 3D方式   rstrid ,cstride 表示图片点与线的跨度
ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap='rainbow')
#contour表示等高线 zdir表示从那个方向压缩
ax.contourf(X,Y,Z,zdir='z',offset=-4,cmap='rainbow')
ax.set_zlim(-2,2)
plt.show()

