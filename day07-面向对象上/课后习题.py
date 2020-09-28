#encoding = utf-8

#1.python中如何通过类创建一个对象
class Student:
    def __init__(self,name,age,num):
        self.name = name
        self.age = age
        self.num = num
        pass

    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

stu = Student("lhh",20,2020)  #创建一个实例对象

# 3.定义一个水果类，然后通过水果类，创建苹果对象，橘子对象，西瓜对象并分别添加上颜色属性
class Fruit:
    def __init__(self,name,color):
        self.name = name
        self.color = color
        pass

    def __str__(self):
        return '%s 是 %s 的' % (self.name,self.color)
        pass

xigua = Fruit("西瓜","绿色")
juzi = Fruit("橘子","黄色")
pingguo = Fruit("苹果","红色")
print(xigua)

#4.编写函数，证明self就是实例本身体
class Demo:
    def __init__(self):
        print("self地址是:%d" % id(self))
        pass

lhh = Demo()
print("实例对象地址:%s" % id(lhh))   #证明self和实例对象地址相同即可

'''
    5.定义一个animal类
        使用_init_初始化方法为对象添加初始属性，如颜色，名字，年龄
        定义动物方法 ，如run ,eat等方法，调用eat,打印正在吃东西即可
        定义一个_str_输出对象的所有的属性
'''
class Animals:
    def __init__(self,color,name,age):
        self.color = color
        self.name = name
        self.age = age
        pass

    def run(self):
        '''
        跑
        :return:
        '''
        print("%s的%s 正在跑" % (self.color,self.name))
        pass

    def eat(self):
        '''
        吃
        :return:
        '''
        print("%s的%s 正在吃" % (self.color, self.name))
        pass

    def __str__(self):
        return "%s的%s 今年%d了" % (self.color,self.name,self.age)

laohu = Animals("黄色","老虎",20)
shizi = Animals("黄色","狮子",21)
xiongmao = Animals("黑白","熊猫",22)
laohu.eat()
shizi.run()
print(xiongmao)