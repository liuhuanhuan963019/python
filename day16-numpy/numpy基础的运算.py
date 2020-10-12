import numpy as np
a = np.array([10,20,30,40])
b = np.arange(4)
print(a)
print(b)

#两个数组相减
c = a-b
print(c)

#两个数组相加
c = a+b
print(c)

#输出平方
c = b ** 2
print(c)

#乘以一个sin值  或cos tan 一样
c = 10 * np.sin(a)
print(c)

#判断某个数与数据元素中的大小
print(b>3)  #[False False False False]
print(b == 3) #[False False False True]


#..................二纬矩阵运算
a = np.array([[1,1],[0,1]])
b = np.arange(4).reshape(2,2)

c = a * b   #元素对应位置直接相乘

c_dot = np.dot(a,b)   #正常的矩阵相称的方式
c_dot_2 = a.dot(b)   #与上面一种表方式完全相同

print(c)
print(c_dot)
print(c_dot_2)



#输出2行3列的随机数字组成的数组
a = np.random.random((2,3))

print(a)
#axis =  0  表示列   1表示行
print(np.sum(a,axis=1))  #输出数组中所有元素的值   求行元素的和
print(np.max(a,axis=0))  #输出数组中所有元素的最大值 求每列元素的最大值
print(np.min(a,axis=1))  #输出数组中所有元素的最小值 求每行元素的最大值

 
