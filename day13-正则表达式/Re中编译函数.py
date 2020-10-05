'''
    re.compile()方法
        compile 将正则表达式模式编译成一个正则表达式对象
        reg = re.compile(pattern) result = reg.match(string)
        等效于 result = re.match(pattern,string)
        使用re.compile()和保存所产生的正则表达式对象重用效率更高

    compile re 模块中的编译方法  可以把一个字符串编译成字节码
    优点：在使用正则表达式进行，match的操作时，python会将字符串转为正则表达式对象
    而如果使用compile则只需要完成一次转换即可，以后再使用模式对象的话，无需重复转换

'''
import re
# reobj = re.compile('\d{4}')
# #开始去使用模式对象reobj
# rs = reobj.match('12345678')
# print(rs.group())
#
# print(re.match('\d{4}','12345678').group())


#re.search   规则是：在全文中匹配一次，匹配到就返回
# data = '我爱中国，I Love China,China is a great country'
# res = re.search('great',data)
# print(res)
# if res:
#     print(res.group())
# print(data[19])
# print(data[20])


#re.findall方法
#findall匹配所有返回一个列表
#findall 匹配所有返回一个列表，这个方法使用频率较高
#        语法：findall(string,[,pos[,endpos]])
#               string     待匹配到字符串
#               pos        可选参数，指定字符串到起始位置，默认为0
#               endpass    可选参数。指定字符串到结束位置，默认为字符串到长度
# data = '华为是华人到骄傲'
# rs = re.findall('华.',data)
# rsearch = re.search('华.',data)
# print(rs)


#改造一下使用compile
# reobj = re.compile('华.')  #创建一个正则对象转换
# print(reobj.search(data))
# print(reobj.findall(data))

#re.sub   实现目标的搜索和查找   以元组形式
# dataS = 'Python是很受欢迎的语言'
# pattern = '[a-zA-Z]+'  #字符集的范围+号代表前导字符模式出现1次以上
# res = re.sub(pattern,'java',dataS)
# print(res)

#re.subn  实现目标的搜索和替换，  返还被替换的数量 以远足的形式
dataS = 'Python是很受欢迎的语言'
pattern = '[a-zA-Z]+'  #字符集的范围+号代表前导字符模式出现1次以上
# res = re.sub(pattern,'java',dataS)
res = re.subn(pattern,'java',dataS)
print(res)    #('java是很受欢迎的语言', 1)


#re.split  实现分割字符串
data = 'baidu,tengxun,阿里，华为，360'
print(re.split(',',data))


#




