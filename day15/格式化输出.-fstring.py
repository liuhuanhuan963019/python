#encoding=utf-8
'''
    f-string 又叫字符串常量  格式化字符串
    f-string在形式上是以f或F修饰符引领的字符串(f'xxx'或F'xxx')
    以大括号{}表明被替换的字段。f-string在本质上并不是字符串常量，而是一个在运行时求值的表达式
'''
name = 'sky'
age = 18
print(f'name is {name},age is{age}.')
#print  name is sky,age is18.

fruits = {'apple':'red','banana':'yelllow'}
s = F"The apple is {fruits['apple']},the banana is {fruits['banana']}"
#f-string 内的引号与外面的引号不能相同，否则会解析失败
print(s)
#print The apple is red,the banana is yelllow

s = 'l love you'
print(f'the reverse is "{s[::-1]}"')
#print the reverse is "uoy evol l"
#逆置也可以的"".join(reversed(1))


#大括号包含可执行的语句
print(f'the set is {{1}}')  #print the set is {1}
print(f'{{{6}}}')  #print  {6}  表达式是整数6
print(f'{{{{6}}}}')  #{{6}}  这里表达式是集合{6}


#example.........................................
import datetime
d = datetime.datetime.now()  #获取当前时间

s = f'{d:%Y-%m-%d%A%p%H:%M:%S.%f}'
print(s)                 #2020-10-12MondayAM00:48:51.810745

s = f'{d:%F}'
print(s)                 #2020-10-12

s = f'{d:%D}'
print(s)                 #10/12/20

s = f'{d:%d%b%Y}'
print(s)                 #12Oct2020

s = f'{d:%X}'
print(s)                 #00:50:54




'''
    f-string大括号中也可以用lamdba，但是会被误认为是表达式与格式描述符之间的分隔符，
    为了避免奇异，需要将lamdba表达式置于括号内（）
'''
l = [1,2,3,4,5]
s = f'求列表每个数的平方:{(lambda x:[y*y for y in x])(l)}'
print(s)

#求列表每个数的平方:[1, 4, 9, 16, 25]
#lambda必须要用括号扩起来，不然无法解析f-string内容，要调用时，方法为:
        # -------------------------------------(lambda函数)(*args,*kwargs)


#_str_和_repr_方法处理对象呈现为字符串，需要在类中定义这些方法，入股必须选一个，需要使用
#_repr_()   它可替代_str_()
#_str_()返回的字符串是对象的非正式字符串表示，可读，_repr_()返回的是官方明确的
#调用str()和repr()比使用_str_()和_repr_()更好
#默认情况下 f字符串使用_str_()方法，若包含!r转换标志，可以确保它们使用_repr_()方法

class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'我的名字是{self.name},今年{self.age}'
    def __repr__(self):
        return f'我的名字是{self.name},今年{self.age} Superise!'

p = Person("lhh",20)
print(f'{p}')   #调用__str__函数
print(f'{p!r}')  #调用__repr__函数



