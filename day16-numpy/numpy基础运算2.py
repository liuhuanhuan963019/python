import numpy as np
#从2-13生成行3*4的矩阵
A = np.arange(2,14).reshape((3,4))
print(A)

#输出A中所有元素最小的元素的下标
print(np.argmin(A))  #0

#输出A中所有元素最大的元素的下标
print(np.argmax(A))   #11

#输出矩阵的平均值
print(np.mean(A))  #7.5
print(A.mean())  #等价 #7.5
print(np.mean(A,axis=0))  #0  表示对列求平均，1 表示对行求平均


#输出矩阵的中位数
print(np.median(A))   #7.5

#累加值
'''
[[ 2  3  4  5]
 [ 6  7  8  9]
 [10 11 12 13]]
[ 2  5  9 14 20 27 35 44 54 65 77 90]
'''
print(A)
print(np.cumsum(A))


#两个数的差
'''
   [[ 2  3  4  5]
    [ 6  7  8  9]
    [10 11 12 13]]
    [[1 1 1]
    [1 1 1]
    [1 1 1]] 
'''
print(A)
print(np.diff(A))


#判断非0
'''
    [[ 2  3  4  5]
    [ 6  7  8  9]
    [10 11 12 13]]
    (array([0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]), array([0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]))
'''
print(A)
print(np.nonzero(A))

#对矩阵进行按行排序
print(np.sort(A))

#将矩阵进行行变列，列变行
'''
    [[ 2  3  4  5]
 [ 6  7  8  9]
 [10 11 12 13]]
[[ 2  6 10]
 [ 3  7 11]
 [ 4  8 12]
 [ 5  9 13]]
[[ 2  6 10]
 [ 3  7 11]
 [ 4  8 12]
 [ 5  9 13]] 
'''
print(np.transpose(A))
print(A.T)   #效果同上
print((A.T).dot(A))   #逆置矩阵乘法


#指定矩阵中大n的数等于n 小于m的数等于m,只输出中间的数 np.clip(A,m,n)
'''
    [[5 5 5 5]
 [6 7 8 9]
 [9 9 9 9]]
'''
print(np.clip(A,5,9))




