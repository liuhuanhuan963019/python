import numpy as np

A = np.arange(12).reshape(3,4)
print(A)

#根据行进行分割
print(np.split(A,2,axis=1))  #根据行分成两组两个列
''' 
    [array([[0, 1],
       [4, 5],
       [8, 9]]), array([[ 2,  3],
       [ 6,  7],
       [10, 11]])]   
'''

#等效分割
print(np.split(A, 1, axis=0))  # 根据列分成两组两个列
'''
    [array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])]
'''

#不等效的分割
print(np.array_split(A, 1, axis=0))  # 根据列分成两组两个列


#进行横向和纵向的分割
print(np.vsplit(A,3))  #纵向分割
# [array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([[ 8,  9, 10, 11]])]
print(np.hsplit(A,2))  #横向分割
'''
    [array([[0, 1],
       [4, 5],
       [8, 9]]), array([[ 2,  3],
       [ 6,  7],
       [10, 11]])]
'''
