# import datetime
# def datetime_datetime_strptime():
#     _datetime = datetime.datetime.strptime(
#         "2018-09-09 18:47:30",
#         "%Y-%m-%d %H:%M:%S"
#     )
#     print(str(_datetime))
#
#
# def datetime_datetime_strftime():
#     now = datetime.datetime.now()
#     print(now.strftime("%Y/%m/%d"))   # 2018/09/09
#     print(now.__format__("%Y/%m/%d")) # 2018/09/09
#
#
# if __name__ == '__main__':
#     datetime_datetime_strftime()
#     datetime_datetime_strptime()
import datetime


#strptime的用法 传入的第一个参数可以是str类型
first_time = datetime.datetime.strptime('2018-02-09','%Y-%m-%d')
print(str(first_time))

#传入的第一个参数必须要是日期类型的数据
now = datetime.datetime.now()
time = datetime.datetime.strftime(now,'%Y-%m-%d')
print(time)
