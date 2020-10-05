import re


#｜ 匹配左右任意一个表达式   实际上是一个或到关系
# string = 'wwyyysqdd8888'
# # rs = re.match('(wwyyysqdd|wwyyysqdd8888)',string)
# rs = re.match('(wwyyysqdd8888|wwyyysqdd)',string)
# print(rs.group())


#(ab) 将括号中到字符作为一个分组 将括号中的字符作为一个分组
#匹配电话号码：xxxx-123456789

#^有两种含义  1.以xxxx开头   2.否定   取反
# res = re.match('([0-9]*)-(\d*)','0517-123456789')
# if res:
#     print(res.group(0))
#     print(res.group(1))
#     print(res.group(2))


#\num 的使用
# htmlTag = '<html><h1>测试数据</h1></html>'
# res = re.match(r'<(.+)><(.+)>(.+)</\2></\1>',htmlTag)
# print(res.group(1))
# print(res.group(2))
# print(res.group(3))


#分组  别名的使用（？P<名字>）
#如何使用别名  （?P=引用的名字）
data = '<div><h1>www.baidu.com</h1></div>'
res = re.match(r'<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>',data)
print(res.group())

