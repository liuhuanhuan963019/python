#encoding=utf-8

'''
    1.接受n个数字，求这些参数数字的和
    2.找出传入的列表或元组的奇数位对应的元素，并返回一个新的列表
    3.检查传入字典的每一个value的长度如果大于2，那么仅保留前两个长度的内容
        并将新内容返回给调用者
        ps:字典中的value只能是字符串或列表
'''

#接受n个数字，求这些参数数字的和
# def getSum(*args):
#     sum = 0
#     for item in args:
#         sum += item
#         pass
#     return sum
#     pass
# print(getSum(1,2,3,4))
# print("rs={}".format(getSum(1,2,3,4,5,6,7)))
# print("rs=%d" % getSum(1,2,3,4,5,6,7))


#找出传入的列表或元组的奇数位对应的元素，并返回一个新的列表
# def process_func(toupleA):
#     '''
#       :param toupleA: 接受的是一个列表或元组
#     :return: 返回的是一个新建的一个列表对象
#     '''
#     listA = []
#     index = 1
#     for item in toupleA:
#         if item % 2 == 1:
#             listA.append(item)
#             index += 1
#             pass
#         pass
#     return listA
#     pass
#
# print(process_func({21,3,5,5,6,8}))


#检查传入字典的每一个value的长度如果大于2，那么仅保留前两个长度的内容
        # 并将新内容返回给调用者
        # ps:字典中的value只能是字符串或列表
def return_dict(dictA):  #**kwargs
    dicyB = {}
    for key,value in dictA.items():
        if len(value) > 2:
            dicyB[key] = value[:2]  #向新字典中添加数据
            pass
        else:
            dicyB[key] = value
            pass
        pass
    return dicyB
    pass

print(return_dict({'name':'haha','didi':'xixi'}))



