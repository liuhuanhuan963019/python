#encoding=utf-8

#_init_(self)方法  初始化方法，实例化对象的时候自动调用，完成一些初始化设置
#用来定义实例属性和初始化数据的，在创建对象的时候自动去调用
#利用传参的机制可以让类更加灵活
class People:
    def __init__(self,name,age):   #创建新对象的时候自动调用该方法
        self.name = name
        self.age = age
        pass

    def run(self):
        print("{}太大了".format(self.age))
        pass

peo = People("hahah",12)  #实例的参数跟随init函数的定义
peo.run()