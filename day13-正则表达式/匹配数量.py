import re

# * 匹配前一个字符出现0次或者无限次
# res = re.match('[A-Z][a-z]*','My')
# print(res.group())     #My

# res = re.match('[A-Z][a-z]*','AsaswegIII')
# print(res.group())    #Asasweg  先匹配大写，再匹配小写  因为后面匹配到了大写，无发匹配，即输出前面所匹配

# + 匹配前一个字符出现1次或者无限次
# res = re.match('[A-Z]+','Axsdwdw')
# print(res.group())     #A

#匹配符合规范[规则是，不能以数字开头，只能包含字母、 数字、下划线]到python变量
# result = re.match('[a-zA-Z_]+[\w]*','_name')
# print(result.group())



#?告诉引擎匹配前导字符0次或者一次，事实上表示前导字符是可以选择到
# result = re.match('[a-zA-Z]+[0-9]?','n299m_e')
# print(result.group())

#{count} 精确匹配
# result = re.match('\d{4}','124467554')
#{min,} max 被省略到话，表示max没有限制了
#{min,max}   告诉引擎匹配前导字符min次到max次，min到max必须都是非负整数
# result = re.match('\d{4}','1211212143565798742344756634')
# result = re.match('\d{4,8}','1211212')
# if result:
#     print("匹配成功:{}".format(result.group()))
#     pass



#匹配邮箱demo   格式xxxxxxx@163.com
regexMail = re.match('[a-zA-Z0-9]{6-11}@163.com','wdwdw@163.com')
if regexMail:
    print('匹配成功：{}'.format(regexMail.group()))
    pass









