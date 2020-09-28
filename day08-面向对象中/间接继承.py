
'''

    总结：我们把父类叫做基类，子类又叫派生类，父类的属性和方法都可以一级一级的传递到子类
    重写就是子类中o
'''

class GrandFather():
    def eat(self):
        print("喜欢吃芒果")
        pass
    pass

class Father(GrandFather):
    def eat(self):
        print("子类重写了")
    pass

class Son(Father):
    pass

son = Son()
print(Son.mro())
fa = Father()
fa.eat()  #重写了父类方法
son.eat()  #此方法是从父类的父类中继承过来的


