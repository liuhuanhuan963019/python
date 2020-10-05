'''
    python字符串中\作为转义字符开头，比如\n表示换行，\t表示tab键，为了表示\本身，再加一个\，成为
    \\形式，在python表示路径，'g:\py资料\1-上课资料\4-正则表达式课件\html'
'''
import re
# print(re.match('c:\\a.txt','c:\\a.txt').group())


#常用的匹配规则-原生字符串

#常用匹配规则
#   ^匹配字符串开头
#   $匹配字符串结尾



#   ^匹配字符串开头
# res = re.match('^P.*','Python is your mum')
# res = re.match('^P\w{5}','Python is your mum')
# if res:
#     print(res.group())


#   $  匹配邮箱到结尾
result = re.match('[\w]{5,15}@[\w]{2,3}.com$','aaaaaaaa@qq.com')
if result:
    print(result.group())