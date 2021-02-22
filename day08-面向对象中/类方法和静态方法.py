'''
    类方法就是类对象所拥有的方法，需要用装饰器@classmethod来标实为类对象，对于类方法，第一个参数必须是类对象
    一般以cls作为第一个参数，类方法可以通过类对象和实例对象调用


    使用静态方法的主要原因：
        由于静态方法主要存放逻辑性的代码，本身和类以及实例对象没有交互
        也就是说，在静态方法中，不回涉及到类中方法和属性的操作
        数据资源能够得到充分有效的利用
'''
class People:
    country = "china"
    #类方法用@classmethod来修饰
    @classmethod
    def get_country(cls):
        return cls.country  #访问类属性
        pass
    pass

    @classmethod
    def chang_country(cls):
        cls.country = "china nanjing"    #类属性在类方法中得到修改
        pass

    @staticmethod
    def getData():
        return People.country   #静态方法中通过类对象去引用
        pass

    @staticmethod
    def add(x,y):      #带有参数的静态方法
        return x+y
        pass
lhh = People()
print(lhh.get_country())     #通过实例对象去访问
print(People.get_country())   #通过类对象去引用
print(lhh.add(10,20))

print("..........change..........")
People.chang_country()
print(People.country)

print("................静态方法的使用..............")

'''
    类对象所拥有的方法，需要用@staticmethod来表示静态方法，静态方法不需要任何参数：
'''

# print(People.getData())    #可以通过类对象.静态方法获取到数据
# pe = People()
# print(pe.getData())    #也可以通过实例对象的方式获取
#！！！一般情况下不回通过实例对象去访问静态方法
import time   #引入时间的
class TimeTest:
    def __init__(self,hour,min,second):
        self.hour = hour
        self.min = min
        self.second = second
        pass

    @staticmethod
    def getTime():
        return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())  #获取当前的时间
        pass
    pass

print(TimeTest.getTime())   #直接调用静态方法显示当前时间
t = TimeTest(10,2,1)
print(t.getTime())   #此时调用的还是静态方法  传递的参数并没有实际运用到