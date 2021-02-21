import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'data/death_valley_2018_simple.csv'

with open(filename) as f:
    #读取文本中的信息，返回一个与文件相关联的文本阅读器
    reader = csv.reader(f)
    #next调用一次表示读取一行元素
    header_row = next(reader)

    # Get dates, and high and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        #将列表中的时间格式转换为固定的格式
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        # 读取文件是可能出现，某一天的数据不存在，读取时可能存在一场，需要异常处理下
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            #固定f-string 常量字符串的应用！！！！
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
#绘制最高气温为红色
ax.plot(dates, highs, c='red', alpha=0.2)
#最低气温为蓝色
ax.plot(dates, lows, c='blue', alpha=0.5)
#两者之间的颜色空格设置为蓝色，透明度为0.1
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
title = "Daily high and low temperatures - 2018\nDeath Valley, CA"
#设置标题
plt.title(title, fontsize=20)
#设置x轴标签内容
plt.xlabel('', fontsize=16)
#设置日期样式倾斜显示
fig.autofmt_xdate()
#设置y轴标签内容
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()