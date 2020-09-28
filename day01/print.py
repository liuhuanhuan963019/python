#-*- coding:utf-8 -*-      解决中文乱码问题
#print('我的')


import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#转译字符  \n 换行  \t制表符   \"    \\

#print ('二狗子：\n','\t我好想你啊')
#java  中用final定义常量
#python  中使用纯大写字母来定义
NAME = "我好想你"
print (NAME)

#'''输出文本内容格式输出
message='''
    狗子：
        我真的好想你啊
'''
print (message)
#三引号的使用
'''
    1.保留格式的字符串使用
    2.作为注释使用
    3.若前面加上赋值符号则是字符串的输出，否则是多行注释
'''
