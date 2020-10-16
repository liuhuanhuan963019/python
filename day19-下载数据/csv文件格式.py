'''
    文件存储数据，最简单的就是将数据作为一系列以逗号分割的值（csv）
    写入到文件当中去
'''
import csv

file_name = 'sitka_weather_07-2018_simple.csv'

with open(file_name) as f:
    # 读取文本中的信息，返回一个与文件相关联的文本阅读器
    reader = csv.reader(f)
    # next()  函数调用一次，读取文件的第一行  此时只读取了，文件的第一行 将reader阅读器对象传递给了next
    #返回一个next()
    header_row = next(reader)
    # print(header_row)
    # ['STATION', 'NAME', 'DATE', 'PRCP', 'TAVG', 'TMAX', 'TMIN']
    #使用enumerate来获取每个元素的索引以及值
    for index,column_header in enumerate(header_row):
        print(index,column_header)

    '''
            0 STATION
            1 NAME
            2 DATE
            3 PRCP
            4 TAVG
            5 TMAX
            6 TMIN
    '''
