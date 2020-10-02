'''
    动态的添加属性和方法
'''
import types
def dymicMethod(self):
    print('{}体重是:{}  今年{}岁了'.format(self.name,People.weight,self.age))
    pass

@classmethod
def classTest(cls):   #类方法必须要有参数cls，否则会报错
    print("这是一个类方法")
    pass

@staticmethod
def staticMethodTest():
    print("这是一个静态方法")
    pass

class People:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return "{}今年{}岁了".format(self.name,self.age)
        pass
    pass

zhangsan = People("zhangsan",20)


zhangsan.weight = 80    #动态的添加了属性，但是只有该实例对象有该属性
zhangsan.printInfo = types.MethodType(dymicMethod,zhangsan)  #给实例对象动态绑定方法
People.weight = 100
print("。。。。。。。。。。。。。。执行实例对象动态的方法调用。。。。。。。。。。。。。")
zhangsan.printInfo()  #调用动态绑定的方法

print("类方法的创建与调用......................")
People.methods = classTest
People.methods()

print("实例对象调用类方法......................")  #实例对象调用类方法依旧可以调用成功
zhangsan.methods()

print("类创建静态方法和调用.....................")
People.staticMethodDemo = staticMethodTest
People.staticMethodDemo()


print(zhangsan)
print(zhangsan.weight)
lisi = People("lisi",30)
print(lisi)
# print(lisi.weight) 会报错

print("给类对象动态的添加属性，添加后每个实例对 象都有该属性......")
People.size = 'z'
print(lisi.size)
print(zhangsan.size)


print("动态的去添加方法。。。。。。。。。。。。。。。。。。。。。。。")
