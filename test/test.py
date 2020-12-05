#encoding=utf-8
import numpy as np
import pandas as pd

data = pd.read_excel("../day17-pandas/demo.xlsx")
print(data)

info_mrarks = pd.DataFrame(data)
writer = pd.ExcelWriter("demo.xlsx")
info_mrarks.to_excel(writer)
writer.save()




