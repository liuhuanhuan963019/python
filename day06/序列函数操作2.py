#encoding=utf-8

'''
    sorted():函数对所有可迭代的对象进行排序操作
    sort与sorted的区别：
        sort使用在list上的方法，sorted可以对所有可迭代的对象进行排序操作
        list对sort方法返回的是对已经存在的列表进行操作，而内建函数sorted方法
        返回的是一个新的list,而不是在原来的基础上进行操作的
    语法：sorted(iterable[,cmp[,key[,reverse]]])
    返回：重新排序的列表
'''

#sort 和sorted
li = [1,32,3,21,42,5]  #原始对象
# li.sort()   #直接对原始对象进行排序
print('排序之前...........................{}'.format(li))
sorted(li)
print('调用sorted后.......................{}'.format(li))   #无变化
listA = sorted(li,reverse=False)   #True 降序     False 顺序
print('重新返回了一个函数...................{}'.format(listA))  #返回函数发生了变化

#reverse（） 函数用于反向列表中的元素   列表中的数据反向输出
#语法  list.reverse()  无返回值
print('调用reverse函数....................')
li.reverse()
print(li)

#range 创建一个整数对列表 [strat,stop[,step]] 默认步长为1
#从start开始  包括start   到stop结束，但是不包括stop


#zip函数  函数用于可迭代对对象，将对象中的对应的元素打包成一个个元组，然后返回由这些元组组成的列表
#存在多余元素则仅显示相应的少的一部分
# s1 = [1,2,3]
# s2 = ['a','b','c']
# print(list(zip(s1)))  #输出[(1,), (2,), (3,)]
# print(list(zip(s1,s2)))  #输出[(1,'a'), (2,'b'), (3,'c ')]

#zip函数的调用
def zip_demo():
    books = []
    id = input("please input:")
    name = input("please input:")
    address = input("please input:")
    idList = id.split(' ')
    nameList = name.split(' ')
    addressList = address.split(' ')
    zipItem = zip(idList,nameList,addressList)
    for item in zipItem:
        itemList = {'id':item[0],'name':item[1],'address':item[2]}
        books.append(itemList)
        pass

    for it in books:
        print(it)
        pass
def zip_userful():
    books=[]
    id = input('please input id space:')
    name = input('please input name space:')
    address = input('please input address space:')
    idList = id.split(' ')
    nameList = name.split(' ')
    addressList = address.split(' ')
    bookInfo = zip(idList,nameList,addressList)
    for item in bookInfo:
        '''
        遍历图书存储
        '''
        dictInfo = {'id':item[0],'name':item[1],'address':item[2]}
        books.append(dictInfo)
        pass

    for item2 in books:
        print(item2)
        pass
    pass

zip_userful()


