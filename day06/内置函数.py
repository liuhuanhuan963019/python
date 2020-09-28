#encoding=utf-8

'''
    内置函数就如同python的扩展函数和扩展库
    https://docs.python.org/3/library/functions.html 内置函数
    常用数学运算的函数
    abs()   求绝对值函数
    round()
    pow()
    divmod()
    max()
    min()
    sum()
    eval()
'''
#abs()   求绝对值函数
print(abs(-2))

#round 对浮点型取近似值，保留几位小数  完全按照四舍五入的方式取值
print(round(3.454,1))

#pow() 求指数
print(pow(3,2))   #9

#max()  返回最大的值
print(max(1,2,3,4,5,6))

#sum()  求和  可以传入一个元组，列表 或集合
print(sum(range(3)))   #3
print(sum(range(3),2))    #指定元素相加   5



'''
    eval() 执行一个字符串表达式，返回表达式的值
    语法：eval(expressional[,globals[.locals]])
    expressional  表达式
    globals 变量的作用域，全局命名空间，如果被提供则必须是一个字典对象
    locas   变量的 作用域，局部命名空间，如果被提供可以是任意映射对象
    返回计算结果
'''
a,b,c=1,2,3
print("动态执行的函数={}".format(eval('a+b+c-20')))
def func():
    print("wo lai la")
    pass

eval('func()')   #可以调用函数执行







