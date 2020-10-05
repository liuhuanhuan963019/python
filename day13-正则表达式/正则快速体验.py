'''
    re.match()从字符串的第一个位置匹配规则，匹配成功返回match对象，匹配失败返回none,
        可以使用group()获取匹配成功的字符串
            re.match(pattern,string,flags=0)
                pattern   匹配的正则表达式
                string  要匹配的字符串
                flags  标志位，用于控制正则表达式的匹配方式  如区分大小和多行匹配等等
'''
import re
data = 'hello world!!!'
result = re.match('h',data)
print(type(result))   #输出<class 're.Match'>
print(result.group())   #匹配成功返回匹配的值




