#encoding=utf-8

#求三组连续自然数的和:求出1-10，20-30和35-45的三个和   sum求和方法
# def sum1(m,n):
#     '''
#     :param m:  开始位置
#     :param n:  结束位置
#     :return:   返回求和结果
#     '''
#     # sum = 0
#     # for item in range(m,n+1):
#     #     sum += item
#     #     pass
#     # return sum
#     return sum(range(m,n+1))
#     pass
#
# print(sum1(1,10))
# print(sum1(20,30))
# print(sum1(35,45))



#2.100个和尚吃100个馒头，大和尚一个吃3个馒头，小和尚三个人吃一个馒头，请问大小和尚各有多少人
# def personCount():
#     '''
#     假设由a个大和尚，100-a个小和尚
#     :return:
#     '''
#     for a in range(1,101):
#         if a * 3 + (100-a)/3 == 100:
#             return (a,100-a)
#         pass
#     pass
# toupleA = personCount()
# print(toupleA[0],toupleA[1])



#3.指定一个列表，列表里包含唯一一个只出现过一次的数字，写程序找出这独一无二的数字
#过滤重复的元素，使用set的原理，无序，无重复性

li = [1,2,3,4,5,3,4,5]
set1 = set(li)   #过滤重复的数字
print(set1)
for i in set1:
    li.remove(i)
    pass
print(li)    #剩余与set1中重复的数字（即至少出现过一次的数字）
set2 = set(li)  #剩余的数字
print(set2)
for j in set1:
    if j not in set2:   #set1中的数字不在set2中就是代表只出现了一次
        print(j)
        pass
    pass




# li = [1,2,3,4,5,4,5,9,2,3,45,6,7,8,9,6,7 ,2]
# set1 = set(li)    #{1, 2, 3, 4, 5, 6, 7, 8, 9, 45}
# print(set1)
# for i in set1:
#     li.remove(i)
#     pass
# print(li)
# set2 = set(li)   #set2 为原来列表中有重复的数字集合
# #若set1中的所有集合在set2中不存在的话，则是不存在的，就是说明了那些数就是
#
# for i in set1:   #set1中数据全部去重后形成的集合
#     if i not in set2:
#         print(i)
#     pass
# pass
