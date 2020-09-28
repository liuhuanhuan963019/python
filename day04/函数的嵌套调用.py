#encoding=utf-8

def fun1():
    print(".................demo1 start")
    print(".................demo1 end")
    pass


def fun2():
    print("..................demo2 start")
    fun1()
    print("..................demo2 end")
    pass

#按顺序执行 先执行调用函数中的代码，然后调用函数中的代码
fun2()