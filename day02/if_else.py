#encoding=utf-8

#单语句
#if 条件表达式：比较运算符 逻辑运算符 /符合的条件表达式
#    代码指令
#    。。。

# score = 70
# if score <= 60:
#     print("不行啊，小老弟")
#     pass  #空语句
#
# print("执行完毕")

#双语句
#if 条件表达式：比较运算符 逻辑运算符 /符合的条件表达式
#    代码指令
#    else
#       代码指令
#pass 表示一个完整的代码块结束了，也可以表示一个空语句 占位符
# score = 70
# if score <=60:
#     print("弟弟行为")
#     pass
# else:
#     print("可以啊，弟弟")
#     pass


#多语句执行
# score = int(input("please input a number..."))
# if score > 90:
#     print("A")
#     pass
# elif score > 80:
#     print("B")
#     pass
# elif score > 70:
#     print("C")
#     pass
# elif score > 60:
#     print("D")
#     pass
# else:
#     print("lj")
#     pass

# import random
# # 0 剪刀  1  石头  2  布
# number = int(input("请输入一个数："))
# computer = random.randint(0,2)
# if number == 0 and computer == 2:
#     print("恭喜你赢了！！！")
#     pass
# elif number == 1 and computer == 0:
#     print("恭喜你赢了！！！")
#     pass
# elif number == 2 and computer == 1:
#     print("恭喜你赢了！！！")
#     pass
# elif number == computer:
#     print("平手")
#     pass
# else:
#     print("you loss")
#     pass

#if else嵌套使用:
score = int(input("please input a number..."))
if score > 90:
    age = int(input("please input a number..."))
    if age < 20:
        print("nb")
        pass
    else:
        print("lj")
else:
    print("zz")
