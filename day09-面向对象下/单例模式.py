'''
    单例模式就是确保一个系统就只有这一个类，一个类只有一个实例
'''
class DataBaseClass(object):
    def __new__(cls, *args, **kwargs):
        #cls._instance = cls.__new__(cls,*args,**kwargs)  不能使用自身的new方法
        if not hasattr(cls,'_instance'):
            cls._instance = super().__new__(cls,*args,*kwargs)
        return cls._instance
    pass

class DbSpring(DataBaseClass):
    pass

test1 = DbSpring()
print(id(test1))
test2 = DbSpring()
print(id(test2))
test3 = DbSpring()
print(id(test3))
#三个实例地址相同，实现了单例模式的创建
