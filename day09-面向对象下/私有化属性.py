'''
    私有化属性：为了不能随意的去修改类属性
    语法：两个下划线开头，声明该属性私有，不能在类的外部被使用和被调用
    class Stu:
        __age = 18  定义了一个私有化的熟悉
    使用场景：
    1.把一个特定的属性隐藏起来，不能让类的外部对象直接调用
    2.想要保护这个属性，不让这个属性的值随意的改变
    3.保护这个属性  ,不想让派生类(子类去继承)

    私有化属性小结：
    1。私有化的实例属性 不能在外部直接的访问，可以在类的内部随意的使用
    2。子类不能继承父类的私有化属性（只能继承父类公共的属性和行为）
    3。在属性的前面加上__可以变为私有化
'''

class People:
    __hobby = "play game"
    def __init__(self):
        self.__name = "李四"  #加上双下划线 将name属性私有化，就不能在类的外部访问，但是在类的内部可以随意访问
        self.age = 30
        pass

    def changeHobby(self):
        self.__hobby = "lol"   #可以在类的内部直接有些私有属性

    def __str__(self):
        return "%s的年龄是%d %s" % (self.__name, self.age, self.__hobby)  # 可以在内部调用私有化属性
        pass

class Student(People):
    def printInfo(self):
        print(self.age)
    pass

stu = Student()
stu.printInfo()
stu.changeHobby()
print(stu)
# print(People.hobby)  #非私有可以直接访问  更改为私有属性无法访问
# print(stu.hobby)  #非私有可以直接访问   更改为私有属性无法访问
# print(stu.__name)  #报错，私有属性，无法继承
x1 = People()
# print(x1.name)   #外部实例对象访问私有化属性失败
print(x1.__str__())
