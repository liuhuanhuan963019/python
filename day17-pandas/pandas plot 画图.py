from __future__ import print_function
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# plot data

# Series
data = pd.Series(np.random.randn(1000), index=np.arange(1000))
data = data.cumsum()   #数据累加
##data.plot()
# data.plot()  #data放到plot

# plt.show()   #plot调用show显示
# # DataFrame
data = pd.DataFrame(np.random.randn(1000, 4), index=np.arange(1000), columns=list("ABCD"))
data = data.cumsum()   #数据累加
# data.plot()
# plt.show()
#   plot methods: plot显示图形的方式
# 'bar'  条形图, 'hist', 'box', 'kde', 'area', scatter', hexbin', 'pie'

#scatter 生成分布点的数据
#scatter 只有x，y两个坐标方式，需要调用在plot的后面
ax = data.plot.scatter(x='A', y='B', color='DarkBlue', label="Class 1")
data.plot.scatter(x='A', y='C', color='LightGreen', label='Class 2', ax=ax)  #我们需要将data附在ax当中需要用ax = ax属性指定

plt.show()  #plot生成图片显示