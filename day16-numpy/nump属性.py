'''
    numpy 处理数据，在机器学习和tensflow等数据处理比python中等list快很多
    顶层使用c语言学习  tensflow神经网络
'''
import numpy as np
array = np.array([[1,2,3],[4,5,6 ]])  #定义数组
print(array)
print("number of dim:",array.ndim)  #几纬数组
print("shape:",array.shape)  #输出行和列
print("size:",array.size)   #输出共有几个元素
