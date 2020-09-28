#encoding=utf-8

#self 与对象指向同一个内存地址，可以认为self就是对象的引用
'''
    self传参问题：
        可以理解为对象自己，某个对象调用其方法时，python解释器会把这个对象作为第一个参数传递给self，
        所以开发者只需要传递后面的参数即可

    self在传递参数的时候不比传值，在调用的时候会默认的去使用自身的函数
    self的名字可以改变，只是默认的定义成这样
    self指的是类实例对象本身  相当于java中的this
'''

class People:
    def say(self):
        print(id(self))
        pass
    pass

lhh = People()
lhh.say()
print(id(lhh))   #两个地址是相同的