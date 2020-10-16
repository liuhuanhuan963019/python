import csv
from datetime import datetime
import matplotlib.pyplot as plt

file_name = '文件读取_csv/data/death_valley_2018_simple.csv'
with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates,highs = [],[]
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)

        highs.append(row[4])

    #绘制数据图形
    fig = plt.figure(dpi=28,figsize=(10,6))
    plt.plot(highs,c = 'red')

    #设置图形的格式
    #设置标题
    plt.title("Daily high temperatures",fontsize = 24)
    #设置x轴添加标签
    plt.xlabel('',fontsize = 24)
    #绘制斜的日期标签
    fig.autofmt_xdate()
    #设置y轴添加标签
    plt.ylabel('temperature(F)',fontsize=24)
    plt.tick_params(axis='both',which='major',labelsize=16)

    plt.show()




