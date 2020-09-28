#encoding=utf-8

'''
    enumerate() 函数用于将一个可遍历的数据对象（如列表。元组，字符串）组成一个索引序列
    同时列出数据和数据下标，一般用在for循环中
'''


# list = [1,2,3,4,5,6]
#
# for item in enumerate(list):
#     print(item)
#     '''
#         输出：(1, 2)
#             (2, 3)
#             (3, 4)
#             (4, 5)
#             (5, 6)
#     '''

# for index,value in enumerate(list,3):
#     print(index,value)
#     '''
#         输出：(3, 2)
#             (4, 3)
#             (5, 4)
#             (6, 5)
#             (7, 6)
#     '''

dictA = {}
dictA['id'] = 12
dictA['name'] = '彩云'
dictA['address'] = '涟水'
print(dictA)

for item in enumerate(dictA):
    print(item[1])
    '''
        输出:id
            name
            address
            
    '''
for item in enumerate(dictA):
    print(item[0])
    '''
        输出:
            0
            1
            2
    '''
for index,item in enumerate(dictA):
    print(item)
    '''
        输出:id
            name
            address

    '''
