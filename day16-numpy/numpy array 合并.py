import numpy as np

A = np.array([1,1,1])
B = np.array([2,2,2])

#合并两个集合为二维
print(np.vstack((A,B)))
''' 
    [[1 1 1]
    [2 2 2]]
'''
C = np.vstack((A,B))
print(A.shape,C.shape)
#print     (3,) (2, 3)

#将两个集合中的所有元素合并到一个集合中去
print(np.hstack((A,B)))   #[1 1 1 2 2 2]

#在行上添加上一个维度
print(A[np.newaxis,:])
print(A[np.newaxis,:].shape)
'''
            [[1 1 1]]
            (1, 3)
'''

#在列上添加上一个维度
print(A[:,np.newaxis])
print(A[:,np.newaxis].shape)
'''
            [[1]
            [1]
            [1]]
            (3, 1)
'''
A = np.array([1,1,1])[:,np.newaxis]   #左行右列
B = np.array([2,2,2])[:,np.newaxis]   #左行右列
D = np.hstack((A,B))
print(D)
'''
    [[1 2]
    [1 2]
    [1 2]]
'''

#0  表示列，    1     表示行
E = np.concatenate((A,B,B,A),axis=0)   #可以进行多个合并，指定在不同维度上进行合并
print(E)




