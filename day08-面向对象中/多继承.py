
class shenxian:
    def fly(self):
        print("can fly")
        pass

class monkey:
    def detail(self):
        print("a monkey")
        pass

class sunwukong(shenxian,monkey):
    pass

# swk = sunwukong()
# swk.fly()
# swk.detail()  #均拥有两个父类中的方法

#当多个父类当中存在相同方法的时候，应该调用哪一个呢
class D(object):
    def eat(self):
        print('D.eat')
        pass
    pass

class C(D):
    def eat(self):
        print('C.eat')
        pass
    pass

class B(D):
    pass
class A(B,C):
    pass

a=A()
a.eat()
print(A.__mro__)  #可以显示类的一次继承的顺序
#查找顺序， 先去A中寻找，找不到去B中寻找，找不到去C中寻找，找不到去D中寻找，再找不到，就报错
#也是继承的顺序