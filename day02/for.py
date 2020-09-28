#encoding=utf-8

#for循环
#语法特点：遍历操作 依此取集合容器中的每个值
#for 零食变量 in 容器
#      代码块

# message = "我爱你"
# for item in message:
#     print(item)
#     pass

#range 此函数可以生成一个数据集合列表
#range(起始:结束:步长)  步长不能为0
# count=0
# for data in range(1,101):    #包含左边不包含右边
#     count += data
#     print(data,end=" ")
#     pass
# print()
# print(count)


index = 0

# for data in range(1,100):
#     if index > 100:
#         print("循环到%d" % data)
#         break;
#         pass
#     index += data
#     pass
# print(index)

# for data in range(1,100):
#     if data % 2 == 0:
#         continue
#         pass
#     else:
#         print(data,end=" ")
#         pass
# print()
# for dat in "l love you":
#     if dat == 'o':
#         continue
#         pass
#
#     print(dat,end=" ")

#99乘法表
# for row in range(1,10):
#     for col in range(1,row+1):
#         print("%d*%d=%d" % (row,col,row*col),end=" ")
#         pass
#     print()
#     pass

#for - else使用   只要for中出现了break else中的语句就不会被执行
# for data in range(1,10):
#     if data > 3:
#         break
#         pass
# else:
#     print("sb")
#     pass

#登陆实例：
# account = "lhh"
# password = "123"
# for num in range(1,4):
#     zh = input("please:")
#     ch = input("please:")
#     if zh == account and ch == password:
#         print("ok")
#         break
#         pass
#     pass
# else:
#     print("用户锁定")
#     pass
index = 0
while index < 10:
    print(index,end=" ")
    if index > 100:
        break
        pass
    index += 1
    pass

else:
    print("到我了")
    pass


