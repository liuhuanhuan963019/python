import numpy as np

z = np.array([[1,2,3,4],[5,6,7,8],[5,6,7,8],[5,6,7,8]])
print(z.shape)
print(z.reshape(-1,1))  #表示n行1列


print(z.reshape(1,-1))  #表示n列1行


print(z.reshape(-1,2))  #表示n行1列
