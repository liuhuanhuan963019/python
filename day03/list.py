#encoding=utf-8

'''
    list python中非常重要的数据结构，是一种有序的数据集合
    特点：
    1。支持增删查改
    2.列表中数据可变但是地址是不变
    3。用[]来表示列表类型
    4。支持索引和切片来进行操作
'''
li = [1,2,3,4,"你好"]
print(len(li))

print(li[1:4]) #输出第二个元素到第四个元素后面的值
print(li[1:])   #输出第二个元素后面所有的元素
print(li[::-1])  #负数从右边开始输出
print(li*2)  #列表中的数据输出两倍

print("追加之前---")
print(li)
li.append("huanhuan")
print(li)
li.append(["dw","dw","qw","111"])
print(li)
li.insert(1,"hah")
print(li)

# del li[0]   #删除指定位置的元素
# print(li)
# del li[1:3]  #删除多项数据
# print(li)
# li.remove(0)
print(li)
li.pop(1)  #移除制定的项 参数是索引值
print(li)


#删除指定元素的值
a = ['a','b','c','d','e','f']
while 'a' in a:
    a.remove('a')

print(a)
