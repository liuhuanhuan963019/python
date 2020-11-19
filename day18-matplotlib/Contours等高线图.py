import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

n=256
x=np.linspace(-3,3,n)
y=np.linspace(-3,3,n)

X,Y = np.meshgrid(x,y)  #将小写的x,y绑定成我们需要输入的值


#设置等高线颜色   alpha=0.75 透明度，cmap='hot'等高线热度
plt.contourf(X,Y,f(X,Y),8,alpha=0.75,cmap ='hot')

#设置等高线样式，color 边颜色为black ,linewidth为
C = plt.contour(X,Y,f(X,Y),8, color='black',linewidth=.5)

#设置等高线的值
plt.clabel(C,inline=True,fontsize=10)
#设置等高线contour
plt.show()