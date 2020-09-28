#encoding=utf-8

'''
    1。字典的key 和value不能重复
    2。字典的key只能是不可变类型（数字，字符串，元祖）
    由键值对组成 类似map集合
    特点：
    1。不是序列类型 没有下标的概念 是一个无序的键值集合  是内置的高级数据类型
    2。用{}来表示字典  每个键值用逗号分开
    3。键必须是不可变的类型【元组，字符串】 值可以是任意类型d
    4。每个键必须是唯一的，如果存在重复的键，后者会覆盖前者
'''

#如何创建字典

# dictA = {'address':'涟水'} #空字典
# dictA['name'] = 'liuhuanhuan'  #可以将次添加到字典中
# dictA['age'] = 8
# print(dictA)

# print(len(dictA))
# print(dictA['address'])  #通过键查找指定的元素
# dictA['address'] = '南京'  #可直接修改键的值
# print(dictA['address'])

# dictA.update({'age':20}) #update 可添加可修改
# dictA.update({'wocao':2323})
# print(dictA)
#删除
# del dictA['name']   #通过键来删除
# dictA.pop('name')   #通过键来删除
#获取所有的键
# print(dictA.keys())
#获取所有的值
# print(dictA.values())


#排序
# print(sorted(dictA.items(),key=lambda d:d[0]))

#获取所有键值对的值
# print(dictA.items())

# for key,value in dictA.items():
#     print("%s:%s" %(key,value))

#共同拥有的方法-------------------------------------
#字符串的合并
str1 = 'wo'
str2 = 'ai'
str3 = 'ni'
print(str1 + str2 + str3)
#list合并
listA = list(range(11))  #不包括11
listB = list(range(11,21)) #左闭右开
print(listA+listB)
#复制
print(listA*2)

#in 对象是否存在 返回一个bol类型的值
print('o' in str1)





