#encoding = utf-8

'''
    集合也是python中的一种数据类型，是一个无序且不重复的元素集合
    创建集合的方式：
    set1 = {"1","2"}
    list1 = ['1','2','3']
    set2 = set(list1)
    操作的函数：
    add() clear() difference() intersection() union() pop() discard() update()
    set不支持索引和切片 是一个无序且不重复的容器
    类似于字典的定义方式，但是字典是key：value的形式，集合是只有key
'''
# dictA = {}
# print(type(dictA)) #dict
# setA = {1,2,3}
# print(type(setA)) #set
#add
# setA.add('21')
# print(setA)

#clear
# setA.clear()
# print(setA)   #set()

#difference() 两个差集  a中存在，b中不存在
set1 = {1,2,3}
set2 = {3,4,5}
# print(set1.difference(set2))   #{1,2}
# print(set1-set2)        #{1,2}  两种表示方式相同

#intersection() 两个交集
# print(set1.intersection(set2))   #{3}
# print(set1&set2)   #{3} 两种 表示方法相同

#union   并集操作
# print(set1.union(set2))   #{1,2,3,4,5}
# print(set1 | set2)    #{1,2,3,4,5}   两种方法相同

#pop就是从集合中拿数据并删除他
# print(set1)    #{1,2,3}
# print(set1.pop())  #1
# print(set1)   #{2,3}

#discard 移除指定的元素
# print(set1)
# print(set1.discard(2))  #移除指定的元素
# print(set1)

#update 更新的操作
set1.update(set2)   #将set2中的元素放到set1当中 类似于并集与set1
print(set1)

