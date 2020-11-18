#encoding=utf=8
import numpy as np
#生成一纬数组的方式


#example 1   创建一个一纬数组  左闭右开 从1开始 步长为1  类似等差数列
array = np.arange(start = 1, stop = 6, step = 1)
print(array)
array = np.arange(1, 6, 1)
print(array)
#print [1 2 3 4 5]


#example 2    创建一个等差数列
#np.linspace(start,stop,num,endPoint=True,restep=False,dtype=None)
#等差数列
#num 为数组到长度
#endpoint默认为True,若为False则不包含右端点
#restep默认为False,若为True则输出由数组和步长组成的tuple

#从1到2 生成11个数
array = np.linspace(start = 1,stop = 2,num = 11)
print(array)
#print [1.  1.1 1.2 1.3 1.4 1.5 1.6 1.7 1.8 1.9 2. ]


#example 3   对比数列
array = np.logspace(start = 0,stop = 3, num = 4)
print(array)
#print [   1.   10.  100. 1000.]   base为底   num为生成到数量
#0表示base的0次幂 3表示base的3次幂
array = np.logspace(start = 0,stop = 3, num = 4,base = 2)
print(array)
#两种方式等价
array = 2 ** np.linspace(start = 0,stop = 3,num = 4)
print(array)
#print [1. 2. 4. 8.]




#用reshape将一维数组调整为
array = np.arange(10)
print(array)

#将一纬数组分割成2行5列的二纬数组
# array = array.reshape((2,5))
# print(array)

#调整后的顺序
array = array.reshape((5,2),order='F')
print(array)

'''
    np.zeros(shape,dtype=float,order="c")
       均为0的数组，shape为大小（3，4） 3*4 的矩阵
    np.ones(shape,dtype=float,order
       均为0的数组，shape为大小（3，4） 3*4 的矩阵 
    np.eye(N,M=none,k=0,dtype=<class 'float'>,order="c")
        创建二纬数组，N是行数，M是列数（默认行列相等），k是对角线偏移量，正数向上，负数向下
    np.identity(n)
        创建单位矩阵
    np.full(shape,fill_value)
        常数数组，shape是形状，fill_value是要填充的值
    np.empty(shape)
        初始化矩阵
'''
#创建多纬数组（以二纬为列）
#example 4   建立一个均为0的多维数组
array = np.zeros((3,4))
print(array)


#example 5   建立一个均为1的多维数组
array = np.ones((3,4))
print(array)

#example 6 二纬数组
array = np.eye(2,2,1)
print(array)

#example 7 二纬单位矩阵
array = np.identity(2)
print(array)

#example 8       2*2矩阵，值均为10
array = np.full((2,2),10)
print(array)

#example 9       2*2矩阵 初始化矩阵      junpybook 和 pycharm中运行结果不一致
array = np.empty((2,2),dtype=float)
print(array)

#example 10    function函数生成的矩阵
#使用lambda row,col为两个指定的参数， row+col为相加  形成（3，3）的矩阵
array = np.fromfunction(function = lambda row,col : row+col,shape = (3,3))
print(array)




#随机数组  （以二纬数组为例）

#example 11 随机生成不同纬度的数组  3*4数组
array = np.random.rand(3,4)
print(array)


#example 12 随机生成1-11的整数，2*6的矩阵
array = np.random.randint(1,11,(2,6))
print(array)
 
#example 13
#随机生成标准正太分布
array = np.random.randn(3,4)
print(array)


#example 14
#将多纬数组拉直为一纬数组
array = np.array([[1,2],[3,4]])
print(array)
array = array.flatten()
print(array)
array = array.ravel(order="F")
print(array)
