#encoding=utf-8
import matplotlib.pyplot as plt
import csv

from datetime import datetime

file_name = '文件读取_csv/data/sitka_weather_2018_simple.csv'

#读取文件的数据
with open(file_name) as f:
    #将文件读取到reader连接器中
    reader = csv.reader(f)
    #读取首行数据 调用一次next读取一行数据
    header_now = next(reader)

    #定义最高最低日期集合接受数据
    dates,highs,lows = [],[],[]

    #遍历文本阅读器中的内容
    for row in reader:
        #读取序列为2的那一列的元素，以规定的日期格式显示
        current_date = datetime.strptime(row[2],'%Y-%m-%d')
        high = int(row[6])
        low = int(row[5])
        #将获取到的数据都存放到集合当中
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

#设置图形显示的样式
plt.style.use('seaborn')
fig,ax = plt.subplots()
#设置最高气温显示颜色
ax.plot(dates,highs,c='red',alpha=0.5)
#设置最高气温显示颜色
ax.plot(dates,lows,c='blue',alpha=0.5)
#在当日最高和最低气温之间空白处填充透明蓝色
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

#设置列表的样式
plt.title("Daily high and low temperatures - 2018", fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdata()
plt.xlabel('temperature (F)',fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
