import pandas as pd


#read_csv  读取csv格式的数据
#read_excel  读取excel格式的数据
data = pd.read_excel('demo.xlsx')
print(data)


#导出为excel
info_marks = pd.DataFrame(data)
writer = pd.ExcelWriter("demo02.xlsx")
info_marks.to_excel(writer)
writer.save()



