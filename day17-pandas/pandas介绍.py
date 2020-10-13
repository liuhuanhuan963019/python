'''
    numpy是已经序列化好的矩阵或数列
    pandas更像是以恶搞字典型的numpy
    numpy相当于列表的画，pandas就相当于一个字典
    pandas可以给不同的行和不同的列命名
'''
import numpy as np
import pandas as pd
s = pd.Series([1,2,3,np.nan],3,4)
print(s)