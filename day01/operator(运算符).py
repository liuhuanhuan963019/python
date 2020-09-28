#encoding=utf-8
name='admin'

name1 = name

print(id(name),name)
print(id(name1),name1)


#id（） 输出地址空间


name1 = 'admin1'
print(id(name1),name1)
print(id(name),name)

a = 10 

a += 5
print(a)

# += -= /= 只能用在数值运算中


#算数运算符
a=12
b=4

result = a**4   #等价于a的4次方
print(result)

result = a // 4
print(result)  # 13/4 = 3   余 1    只取三


name ="haha"
name1 = "haha"
name2 = "xixi"

print(id(name))   #name地址和name1相同。 因为所赋值对象相同，不会重新申请内存空间
print(id(name1))
print(id(name2))