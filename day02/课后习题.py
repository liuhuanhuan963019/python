"""
1。猜年龄
    允许用户尝试三次
    每尝试三次后询问是否还想继续 y继续 n否
    猜对了 直接退出
2。升高1。75体重80。5根据bmi公式（体重除以身高的平方） 计算BMI指数
低于18。5  很轻
18。5-25  正常
25-28    过重
28-32    肥胖
高于32    严重肥胖
用if-else打印
"""
weight = 80.5
high = 1.75
bim = 80/(1.75**2)
if bim < 18.5:
    print('很轻')
    pass
elif bim >= 18.5 and bim <= 25:
    print('正常')
    pass
elif bim >= 25 and bim <= 28:
    print('过重')
    pass
elif bim >= 28 and bim <= 32:
    print('肥胖')
    pass
else:
    print('严重肥胖')

# number = 10
# index = 0
# while index <= 3:
#     age = int(input("please"))
#     if age == number:
#         print("congrations!!")
#         break
#         pass
#     elif age > number:
#         print("大了")
#     else:
#         print("小了")
#
#     index += 1
#     if index == 3:
#         num = input("输入'Y'或'N'")
#         if num == 'y' or num == 'Y':
#             index = 0
#         else:
#             break
#             pass
#     pass



