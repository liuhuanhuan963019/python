'''
    贪婪模式：
        默认的匹配规则
        在满足条件的情况下经可能多的去匹配到数据
'''
import re

rs = re.match('\d{6,9}','111122234')
# print(rs.group())

content = 'aacbacbc'
pattern = re.compile('a.*b')   #贪婪模式
result = pattern.search(content)
print('非贪婪模式%s' % result.group())    #aacbacb


pattern = re.compile('a.*?b')   #非贪婪模式
result = pattern.search(content)
print('非贪婪模式%s' % result.group())    #aacb

#非贪婪模式
#在满足条件的情况下，尽可能少的去匹配到数据
rs = re.match('\d{6,9}?','21212121')
# print(rs.group())