'''
    numpy是已经序列化好的矩阵或数列
    pandas更像是以恶搞字典型的numpy
    numpy相当于列表的画，pandas就相当于一个字典
    pandas可以给不同的行和不同的列命名
'''
import numpy as np
import pandas as pd

#pandas数据中总是以32位或者是64位的格式来保存的
s = pd.Series([1,2,3,np.nan,3,4])  #pandas的序列
'''
    0    1.0
    1    2.0
    2    3.0
    3    NaN
    4    3.0
    5    4.0
    dtype: float64  #主要形式都是float64
'''
print(s)


dates = pd.date_range('20201015',periods=6)
print(dates)
'''
    DatetimeIndex(['2020-10-15', '2020-10-16', '2020-10-17', '2020-10-18',
               '2020-10-19', '2020-10-20'],
              dtype='datetime64[ns]', freq='D')
'''

df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])
print(df)
'''
            a         b         c         d
2020-10-15  0.423955 -0.309673 -0.017753  0.054436
2020-10-16 -1.482949  0.432019 -0.363933 -1.696985
2020-10-17 -0.117602 -1.096218  1.117089 -1.075847
2020-10-18 -1.453770  1.641181  1.097931 -3.762856
2020-10-19 -1.642981  2.113422 -0.553068 -2.129849
2020-10-20 -0.674258  0.555073  1.043101  0.263870
'''


df1 = pd.DataFrame(np.arange(12).reshape(3,4))
print(df1)
'''
       0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
'''

df2 = pd.DataFrame({
        'A': 1,
        'B': pd.Timestamp('20201015'),
        'C': pd.Series(1,index=list(range(4)),dtype='float32'),
        'D': np.array([3]*4,dtype='int32'),
        'E': pd.Categorical(['test','train','test','train']),
        'F': 'foo'
})
print(df2)
'''
       A          B    C  D      E    F
0  1 2020-10-15  1.0  3   test  foo
1  1 2020-10-15  1.0  3  train  foo
2  1 2020-10-15  1.0  3   test  foo
3  1 2020-10-15  1.0  3  train  foo
'''
print(df2.dtypes)
print(df2.columns)
#Index(['A', 'B', 'C', 'D', 'E', 'F'], dtype='object')

print(df2.describe())
'''
        A    C    D
count  4.0  4.0  4.0
mean   1.0  1.0  3.0
std    0.0  0.0  0.0
min    1.0  1.0  3.0
25%    1.0  1.0  3.0
50%    1.0  1.0  3.0
75%    1.0  1.0  3.0
'''

print(df2.T)
'''
                         0  ...                    3
A                    1  ...                    1
B  2020-10-15 00:00:00  ...  2020-10-15 00:00:00
C                    1  ...                    1
D                    3  ...                    3
E                 test  ...                train
F                  foo  ...                  foo
[6 rows x 4 columns]    
'''
