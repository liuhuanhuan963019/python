#encoding=utf-8

'''
    1.字符串常用方法
    2.切片操作
    3.与其他类型综合操作
    序列：在python当中，序列就是一组按照顺序排列的值
    在python中：存在三种内置的序列类型
    字符串：列表：元祖
    优点：可以支持索引和切片操作
    特点：第一个正索引为0,指向的是左端，第一个索引为负数时指向的是右端
    切片：[start:end:step] step 默认是1
'''

Test = "python"
print(type(Test))

print("获取第一个字符串%s" % Test[0])

for item in Test:
    print(item,end=" ")

print()
name = "liuhuanhuan"
print("姓名变换%s" % name.capitalize())

address = "    淮安   "
print(address.strip())   #去空格

strMsg = "hello world!!!"
print(strMsg[0:3])











