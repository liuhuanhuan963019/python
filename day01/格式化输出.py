#encoding=utf-8
name = '王彩云'
address = '江苏省苏州市'
phone = '15155809309'
age=5
print ('姓名是'+name+' 地址是'+address+' 电话是'+phone)
print ('姓名是%s,地址是%s,电话是%s' %(name,address,phone))
print ('年龄是'+str(age))    #强制类型转换
#digit  数字

#。1f小数点后面保留一位小数，并四舍五入
salary = 292.32
print ("薪水是%.1f\n" % salary)

#使用占位符输出字符串
age=2
name='王彩云'
address='江苏苏州'
message = '今年{}岁了，叫{}，住在{}'.format(age,name,address)
print (message)