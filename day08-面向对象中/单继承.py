'''

    单继承
'''
class Animal:
    def eat(self):
        print("猫在吃")
        pass

    def drink(self):
        print("狗在喝")
        pass

class cat(Animal):   #cat继承了animal类
    def jiao(self):
        print("miamiao")
        pass
    pass

class dog:
    def jiao(self):
        print("wangwang")
        pass
    pass

cat1 = cat()
cat1.eat()
cat1.jiao()