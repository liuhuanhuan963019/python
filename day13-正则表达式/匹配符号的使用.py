import re
#.的使用
# data = 'aaaa'
# parent = '.'
# res = re.match(parent,data)
# print(res.group())   #返回一个a

# names = '李世民','李敏','aha','dss'
# parent = '李..'
# for item in names:
#     res = re.match(parent,item)
#     if res:
#         print(res.group())   #返回一个李世民




#[]的使用，匹配规则是:匹配括号中的任意一个字符
# str1 = 'eee'
# res = re.match('[he]',str1)
# print(res.group())
#
# pattern = '[abc]' #使用中括号扩起来的内容，代表一个集合，代表匹配集合内的任意一个字符
# patter = '[a-z]'  #可以简写一个范围abcdef
# #【abc】代表可以匹配a或者b或者c
# datas = 'a','b','c','e','wyw'
# for data in datas:
#     result = re.match(pattern,data)
#     if result:
#         print('匹配成功 %s' % data)



#\d  匹配一个数字  0-9
# data = '123dsdf'
# print(re.match('\d\d\d',data).group())


#\D  匹配一个非数字
# data = 'w123dsdf'
# print(re.match('\D\d',data).group())    #w1


#\s  匹配一个空白字符或tab键
# data = ' w123dsdf'
# print(re.match('\s',data).group())    #w1


#\S  匹配一个非空白字符或tab键
# data = 'w123dsdf'
# print(re.match('\S',data).group())    #w1


# \w    匹配单词字符   即a-z  A-Z  0-9
# data = 'advs+dwq'
# print(re.match('\w',data).group())


# \W    匹配非单词字符   即[a-z,A-Z]
# data = '@@$$%%advs+dwq'
# print(re.match('\W\W',data).group())


