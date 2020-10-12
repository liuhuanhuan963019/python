import numpy as np
#3-15 组成的3*4的矩阵
A = np.arange(3,15).reshape(3,4)

print(A)
print(A[2])  #输出第三行的数据
print(A[2,:]) #效果同上
'''
    [[ 3  4  5  6]
 [ 7  8  9 10]
 [11 12 13 14]]
[11 12 13 14]
'''
print(A[0][0])

#输出第三列所有的数
print(A[:,2])

#输出第2行第二列第三列的数
print(A)
print(A[1,2:4])
'''
[[ 3  4  5  6]
 [ 7  8  9 10]
 [11 12 13 14]]
        [ 9 10] 
'''

#循环输出
for row in A:
    print(row)  #输出每一行
    '''
        [3 4 5 6]
        [ 7  8  9 10]
        [11 12 13 14]
    '''

#行变列 列变行输出
for colum in A.T:
    print(colum)
    '''
        [ 3  7 11]
        [ 4  8 12]
        [ 5  9 13]
        [ 6 10 14]
    '''

#将矩阵转换成一行
print(A.flatten())
#print     [ 3  4  5  6  7  8  9 10 11 12 13 14]

#循环输出 (上面的值)
for item in A.flat:
    print(item)
