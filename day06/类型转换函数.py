#encoding=utf-8

'''
    类型转换函数：
    int()
    float()
    str()
    ord()
    chr()
    bool()
    bin()
    hex()
    oct()
    list()
    tuple()
    dict()
    bytes()
'''

#chr()  数字转字符
print(chr(45))
print(chr(65))
#bin()转为二进制
#hex()转为十六进制


#元组转换成列表
tup=(1,2,3,4)
li = list(tup)
li.append("ok")
print(li)


#字典操作dict()
dic = dict(name='小明',age=18)
print(type(dic))
print(dic )

 #bytes()
print(bytes('我爱你',encoding='utf-8'))