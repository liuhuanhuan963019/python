#所谓重写就是子类中拥有与父类相同名字的方法，在子类中完全覆盖掉了父类中的方法

class Dog:
    # 此时在父类中定义了init方法，子类中未定义，实例化对象时调用的是父类中的方法，此时报错
    def __init__(self,name,color):
        self.name = name
        self.color = color
        pass

    def fit(self):
        print("狗叫")
        pass
    pass

class Rabbit(Dog):
    def __init__(self,name,color):   #在子类中定义了此方法，重写了父类中的方法
        #若需要像父类中一样拥有此属性，就需要执行这样的代码
        # Dog.__init__(self,name,color)  #调用此方法，执行完毕就具有了name,color两种属性
        super().__init__(name,color)  #此方法与上面的方法具有相同的作用，若继承多个父类，则按照顺序去寻找
        pass
    def fit(self):
        super().fit()  #调用父类的方法
        print("机器狗叫")
        print(self.name)
        pass
    pass

rab = Rabbit("xixi","a")
rab.fit()       #调用了自身的函数,重写父类中的方法
