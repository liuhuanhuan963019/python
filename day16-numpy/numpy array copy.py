import numpy as np

A = np.arange(4)
print(A)   #[0 1 2 3]

B = A   #浅拷贝  B就是A 两个代表的是同一个元素

C = A

D = A

print(B)  #[0 1 2 3]

B[0] = 11
print(A)  #[11  1  2  3]

print(B is A)  #True

D[1:3] = [22,33]
print(D) #[11 22 33  3]
print(A)  #[11 22 33  3]


#如何实现深拷贝呢，值将值传递给另一个参数，而不将地址传过去
B = A.copy()
print(A)  #[11 22 33  3]
print(B)  #[11 22 33  3]

B[1:3] = [10,20]
print(A)  #[11 22 33  3]
print(B)  #[11 10 20  3]