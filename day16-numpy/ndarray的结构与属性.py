# encoding=utf-8

import numpy as np

#空数组
a = []
array = np.array(a)
print("这是一个空数组",array)

#一纬数组
a = range(3)
array = np.array(a)
print("这是一个一纬数组",array)

#二维数组
a = [[1,2],[3,4]]
array = np.array(a)
print("这是一个二纬数组",array)

#二维数组
a = [[1],[2],[3]]
array = np.array(a)
print("这是一个二纬数组",array)
