#encoding=UTF-8

'''
    匿名函数：
    lambda 参数1，参数2，参数3：表达式
    特点：
    使用lambda创建函数 没有名称
    匿名函数冒号后面的表达式有且只有一个，是表达式，不是语句！！！！
    匿名函数自带return,返回的 结果就是表达式计算后的结果
'''
def sum(x,y):
    '''
    求和
    :param x:
    :param y:
    :return:
    '''
    return x+y
    pass

print(sum(10,2))

M = lambda x,y:x+y
print(M(1,2))

age = 20
print('可以yp' if age > 18 else '不可以yp')  #替换传统的if else 语句

result = lambda x,y:x if x>y else y
print(result(10,2))

result = (lambda x,y:x if x>y else y)(12,20)  #相当于直接调用参数传参
print(result)
