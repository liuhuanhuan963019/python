#encoding=utf-8

'''
    元祖：是一种不可变的序列，在创建之后不能做任何的修改
    1。不可变
    2。用（）创建元组，数据用逗号来分割
    3。可以是任意的类型
    4。当元组中只有一个元素，要加上逗号，不然后解释器当作整形来处理
    5。同样支持切片操作
'''

#元组的创建
# tupleA = ()
# print(type(tupleA))
tupleB = ('21',3,32,54,21,5,2,'dd',[1,2,3])
# for item in tupleB:
#     print(item,end=" ")
print(tupleB[::-2])  #每隔两隔选一个数

print(tupleB[-2:-1]) #倒着取下标 为-2到-1区间

#元祖不可被修改
#可对元组列表类型中对数据进行修改
tupleB[8][0] = 520
print(tupleB)

tupleC = ('ds',) #当元组中只有一个元素当时候，需要在后面加上,
tupleD = tuple(range(10))  #range 包左不包右
print(tupleD)