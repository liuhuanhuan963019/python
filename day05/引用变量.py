#encoding=utf-8

'''
    在python，值是靠引用来传递的，可以用id()查看一个
    对象的引用是否相同，id是值保存在内存中那块内存地址
    的标实

    在调用对象过程中，实际传递的是对对象对引用
    参数传递是通过引用来传递的
'''


# a = 1   #不可变类型 一旦确定，值改变会重新开辟一个新的内存空间
# def func(x):
#     x=2   #此时地址已经发生了改变
#     print('地址{}'.format(id(x)))   #地址发生了变化
#     pass
#
# print('地址{}'.format(id(a)))
# func(a)


#可变类型  字典或列表

listA = []
def params(par):
    print(id(par))
    listA.append([21,3,5,57,8])
    pass

print(id(listA))
params(listA)