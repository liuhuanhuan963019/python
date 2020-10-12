import numpy as np
array = np.array([1,2,3],dtype=np.float32)
print(array.dtype)   #float32

#创建一个三行四列，元素都为0的二维数组
array = np.zeros((3,4))
print(array)

#创建一个三行四列，元素都为1的二维数组
array = np.ones((3,4))
print(array)

#创建一个三行四列，元素为空的二维数组
array = np.empty((3,4))
print(array)

#定义10-20步长为2的有序的数列
array = np.arange(10,20,2)
print(array)

#定义一个0-11 的3行4列的数列
arrar = np.arange(12).reshape(3,4)
print(array)

#生成5个1-10之前数字的线段  [ 1.    3.25  5.5   7.75 10.  ]
array = np.linspace(1,10,5)   #加上.reshape(m,n)  定义m,n纬的数组
print(array)


