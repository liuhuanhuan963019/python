

'''
    1.析构函数：
        当一个对象被删除或销毁时，python解释器也会默认调用一个方法，这个方法为_del_()方法，也称为析构函数
        当对象手动删除对象的时候，也会自动去调用del方法
        析构函数一般用于资源回收，利用del方法销毁对象回收内存等资源

'''

class Student:
    def __init__(self):
        print("初始化对象.....")
        pass
    def __del__(self):
        '''
        当在某个作用域下，没有使用（引用）的情况下，解析器会自动调用该函数，来释放内存空间
        主要就是操作对象的释放，一旦释放完毕，对象便不能再使用
        :return:
        '''
        print("调用析构函数，销毁对象....")
        pass

stu = Student()
input("please:")
stu1 = Student()
del stu1