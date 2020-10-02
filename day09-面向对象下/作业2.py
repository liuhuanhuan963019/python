'''
    1.定义一个Person类，类中要有初始化方法，方法中要有人的姓名，年龄两个私有属性
        提供获取用户信息的函数
        提供获取私有属性的方法
        提供可以获取私有属性的方法
        设置年龄范围，如果不在这个范围设置不成功
    2.写一个单例模式
    3.创建一个类，并定义两个私有化属性，提供一个获取属性的方法和设置属性的方法，利用peoperty属性给调用者
'''

# 1.定义一个Person类，类中要有初始化方法，方法中要有人的姓名，年龄两个私有属性
class Person:
    def __init__(self,name,age):
        '''
        :param name:
        :param age:
        '''
        self.__name = name
        self.__age = age

    def __str__(self):
        return "姓名:{}，年龄:{}".format(self.__name,self.__age)

    def get__name(self):
        return self.__name
    def set__name(self,name):
        self.__name = name
    def get__age(self):
        return self.__age
    def set__age(self,age):
        if age > 0 and age < 120:
            self.__age = age
        else:
            print("年龄输出失败")
            pass

 # 2.写一个单例模式
class Student(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,"_instance"):
            cls._instance = super().__new__(cls,*args,**kwargs)
        return cls._instance


 # 3.创建一个类，并定义两个私有化属性，提供一个获取属性的方法和设置属性的方法，利用peoperty属性给调用者
class Animasl:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
        pass

    @property  #装饰器返回一个geteer方法
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name

    @property  # 装饰器返回一个geteer方法
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    def __str__(self):
        return "{}的年龄都是{}".format(self.__name,self.__age)
    def __call__(self, *args, **kwargs):
        print("{}的年龄都是{}".format(self.__name,self.__age))
        pass

bird = Animasl("xiaomiao",20)
bird()    #将实例对象以函数的形式去调用
bird.age = 90
print(bird)

# 4.绑定类属性和类方法
import types
def run(self):
    print("run")
    pass

@classmethod
def methodDemo(cls):
    print("cnm")
    pass

class Animals:
    pass

cat = Animals()
print("类动态绑定属性...................")
Animals.color = "白色"   #类动态绑定属性
print("类动态的绑定方法.................")
cat.runDemo = types.MethodType(run,cat)   #类动态的绑定方法
cat.runDemo()
print("类方法的创建与调用...............")
Animals.methods = methodDemo
Animals.methods()   #成功调用类放方法
print(cat.color)