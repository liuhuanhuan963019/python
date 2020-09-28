#encoding=utf-8
#!/usr/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python3.7

print ("hello world")

#高级数据类型
a = ()   #元祖类型
print (type(a))


a = []    #列表类型
print (type(a))

a = {}    #字典类型
print (type(a))

a=7
b=2
print (a**b)   #49
print (a//b)  #3

name = input("请输入：")   #输入的均是str类型的数据
address = '江苏省苏州市'
phone = '15155809309'
age=5

print ("name=%s" % name)
print ("address=%s" % address)
print ("phone=%s" % phone)
print ("age=%d" % age)


print ("name={}".format(name))