#encoding=utf-8

#如果在函数的内部要想对全局变量进行修改，必须使用global关键字进行修改

name = '小可爱'
address = '涟水'
def input1():
    name = 'aha'
    print('{}'.format(name))
    pass
def input3():
    print('{}'.format(name))
    pass

def input2():
    '''
    改变全局变量
    :return:
    '''
    global name
    name = '我爱你'
    print('{}'.format(name))
    pass

def input4():
    print('{}'.format(name))
    pass
input1()
input3()
input2()
input4()

