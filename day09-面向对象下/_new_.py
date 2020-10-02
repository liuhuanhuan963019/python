'''
    _new_ 方法的作用是，创建并返回一个实例对象，如果_new_只调用了一次，就会得到一个对象。
    继承自object的新式类才有new的这个魔法方法
    warning:
        _new_是在一个对象实例化的时候所调用的第一个方法
        _new_至少必须要有一个参数，代表要实例化的类，此参数在实例化时由python解释器自动提供
        ，其他的参数是用来直接传递给_init_方法
        _new_决定是否要使用_init_方法，因为_init_可以调用其他类的构造方法或者直接返回别的实例对象来
        作为本类的实例，如果_new_没有返回实例对象，则_init_不回被调用
        在_init_方法中，不能调用自己的_new_方法，否则会报错
'''
class Animal:
    def __init__(self):
        self.age = 10
        pass
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls,*args,**kwargs)
        # return object.__new__(cls)
        pass
    pass