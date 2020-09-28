'''
    同一种行为对于不同的子类对象，具有不同的行为表现
    实现多态需要遵循多两个前提：
    1.继承：多态必须发生在父类与子类之间
    2.子类重写父类的方法

'''
class Animals:
    def say(self):
        print("我是一只动物")
        pass
    pass

class Dog(Animals):
    def say(self):
        print("我是一只小猴狗")
        pass
    pass

class Cat(Animals):
    def say(self):
        print("我是一只小猫咪")
        pass
    pass

def commonInvoke(obj):
    obj.say()
    pass
# dog = Dog()
# dog.say()
# cat = Cat()
# cat.say()
listObj = [Cat(),Dog()]    #多态的好处，可以，统一的定义方法分别去调用不同的函数
for item in listObj:
    commonInvoke(item)