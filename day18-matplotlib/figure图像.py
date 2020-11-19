import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.linspace(-1,1,50)
y = x**2
plt.figure(figsize=(10,10))
#color设置实线的颜色，linewidth设置实线的宽度 linestyle设置曲线样式
plt.plot(x,y,color="red",linewidth=1.0,linestyle='--')
plt.show()