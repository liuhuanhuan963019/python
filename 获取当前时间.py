import datetime
import time

# 获取当前时间
now = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
print(now)

now2 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(now2)