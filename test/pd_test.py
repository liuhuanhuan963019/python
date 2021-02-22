import pandas as pd
import numpy as np
#打印指定格式的数据日期  periods 指定往后衍生几天
dates = pd.date_range('20201015',periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])
print(df)


