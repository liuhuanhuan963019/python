import csv
import matplotlib.pyplot as plt
from datetime import datetime

file_name = '文件读取_csv/data/sitka_weather_2018_simple.csv'

#读取文件的数据
with open(file_name) as f:
    # 将文件读取到reader连接器中
    reader= csv.reader(f)

    #读取首行数据 调用一次next读取一行数据
    header_row = next(reader)

    #定义最高最低日期集合接受数据
    highs,dates = [],[]

    #遍历文本阅读器中的内容
    for row in reader:
        #读取序列为2的那一列的元素，以规定的日期格式显示
        current_date = datetime.strptime(row[2],'%Y-%m-%d')
        dates.append(current_date)

        high = int(row[6])
        highs.append(high)

    # 列表图中的折线设置颜色
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    # 划线,最高气温显示
    ax.plot(dates, highs, c='red', alpha=0.5)

    #列表样式的显示(单纯的列表样式)列表图中的折线还需要再重新设置
    plt.title('Daily high and low temperatures - 2018',fontsize=24)
    plt.xlabel('',fontsize=16)
    # 设置日期样式倾斜显示
    fig.autofmt_xdate()
    plt.ylabel('temperature (F)',fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

