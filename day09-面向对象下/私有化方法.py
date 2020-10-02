#encoding = utf-8

''''
    私有化方法一般是类内部调用，子类不能继承，外部不能调用
    单下划线、双下划线、头尾双下划线说明
    _xxx前面只加一个下划线开头的表示的是protected类型的变量，即保护类型只能允许其本身与子类进行访问，
    不能使用from ** import 的方式导入
    _xxx_前后两个下划线，魔法方法，一般是python自带的方法
    xxx_后面单下划线，避免属性名和python关键字发生冲突
'''
class Animals:
    def __eat(self):   #将方法私有化之后 子类继承父类的方法，将不再可以直接使用
        print("eat")
        pass
    def run(self):
        self.__eat()
        print("run")
        pass

class bird(Animals):
    pass

bir = bird()
bir.run()