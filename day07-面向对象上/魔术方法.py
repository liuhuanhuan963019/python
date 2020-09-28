#encoding=utf-8

'''
    内定好的方法，格式如_xxx_的形式，在进行特定的操作的时候会被调用，这些方法被称之为魔术方法
    如：
    _init_   初始化一个类，在创建实例对象为其赋值使用
    _str_    在将对象转成str（字符串）测试的时候，会打印对象的信息
    _new_    创建并返回一个实例对象，调用了一次，就会得到一个对象
    _new_    获得已知对象的类
    _new_    对象在运行结束的时候会自动调用该方法来销毁内存，释放资源
'''

class People:
    def __init__(self,name,age):
        print(".............init 函数执行.................")
        self.name = name
        self.age = age
        pass


    def eat(self):
        print("%s是傻逼" % self.name)
        pass

    def __str__(self):
        print(".............str函数执行.................")
        return "%s 今年 %d 岁了" % (self.name,self.age)
        pass

    def __new__(cls, *args, **kwargs):
        '''
        创建实例化对象的方法，每调用一次就会生成一个新的对象cls就是class的缩写
        可以控制创建对象的一些属性的限定，通常用在单例模式中
        :param args:
        :param kwargs:
        '''
        print(".............new 函数执行.................")
        return object.__new__(cls)    #在这里真正的创建一个实例化对象.......

stu = People("lhh",24)   #自动调用_init_方法
stu.eat()
# print(stu)   #自动调用__str__方法  类似于java中的toString方法

'''
     
'''
