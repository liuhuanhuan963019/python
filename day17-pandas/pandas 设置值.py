from __future__ import print_function
import pandas as pd
import numpy as np

#日期为横向标签，abcd为竖向的标签
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)), index=dates, columns=['A', 'B', 'C', 'D'])

#根据位置来进行选择 设置指定位置的值
df.iloc[2,2] = 1111

df.loc['2013-01-03', 'D'] = 2222

df.A[df.A>0] = 0

# print(df)
'''
            A   B     C     D
2013-01-01  0   1     2     3
2013-01-02  0   5     6     7
2013-01-03  0   9  1111  2222
2013-01-04  0  13    14    15
2013-01-05  0  17    18    19
2013-01-06  0  21    22    2
'''

#新增一列
df['F'] = np.nan

#新增一列序列
df['G']  = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130101', periods=6))
# print(df)
