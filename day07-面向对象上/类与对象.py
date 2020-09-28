#encoding=utf-8

class Student:
    name = "haha"   #类属性
    age = 20
    def __init__(self):
        self.name #实例属性
        pass

    def run(self):   #self很重要的关键字
        print("%s正在跑" % self.name)
        pass

stu = Student()   #创建一个实例化对象
stu.run()