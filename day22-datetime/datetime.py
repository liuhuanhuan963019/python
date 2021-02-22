import datetime

# 获取当前时间
print(datetime.date.today())
# 2021-02-22

#
print(datetime.date.fromtimestamp(1596325456))

d = datetime.date(2021,2,22)
print(d.weekday())

# 获取当前时间
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

import time
print(time.asctime(time.localtime(time.time())))