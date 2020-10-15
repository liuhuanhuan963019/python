# from __future__ import print_function
import pandas as pd
import numpy as np

#以日期排序的行为dates，列为ABCD显示的序列
dates = pd.date_range('20200101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=['A', 'B', 'C', 'D'])

#两种打印方式是一摸一样的
print(df['A'], df.A)
#执行选择输出某几行的数据  两种方式 df[0:3] 和df['20130102':'20130104']效果等效
print(df[0:3], df['20200101':'20130104'])


# select by label: loc  指定根据标签来选择
#以日期的方式显示出来
print(df.loc['20200102'])
'''
    A   -1.726134
    B   -0.194859
    C   -0.571111
    D   -1.584783
Name: 2020-01-02 00:00:00, dtype: float64
'''

#保留行的所有数据，对列进行选择以AB进行选择
print(df.loc[:,['A','B']])
'''
            A         B
2020-01-01  0.382860  0.825605
2020-01-02  0.209191  0.870491
2020-01-03  0.588401 -1.255071
2020-01-04 -1.114446  0.570606
2020-01-05  0.457309 -0.469816
2020-01-06 -0.383009 -0.570806
'''
#

print(df.loc['20200101', ['A','B']])
'''
    A   -0.832464
    B   -2.151533
Name: 2020-01-01 00:00:00, dtype: float64
'''

# select by position: iloc  从某个位置开始选择，类似于numpy中的定位
print(df.iloc[3])   #输出第三行的数据
print(df.iloc[3, 1])  #输出第三行，第一位的数据
print(df.iloc[3:5,0:2]) #输出第三行到第五行，第一位到第三位的数据
print(df.iloc[[1,2,4],[0,2]])  #进行指定某一行来进行筛选
#
# mixed selection: ix  把loc和iloc综合起来筛选
#loc和iloc为纯标签或者纯数字筛选的过程  使用ix可以进行进行标签数字混合筛选
print(df.ix[:3, ['A', 'C']])
# Boolean indexing  进行逻辑选择判断，进行布尔判断
print(df[df.A > 0])