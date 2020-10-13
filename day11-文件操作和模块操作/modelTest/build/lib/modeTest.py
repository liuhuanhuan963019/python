#模块的制作过程

#魔幻数字__all__的使用 如果一个文件中存在__all__变量，那么也意味着这个变量中的元素
#会被from xxx import * 时引用
#对于import方式来说，所有的方法全部被引用了
__all__ = ["add","diff"]

def add(x,y):
    '''
    两个数字相加
    :param x:
    :param y:
    :return:
    '''
    return x+y
def diff(x,y):
    return x-y

def printInfo():
    return "自定义方法.........."

if __name__  == '__main__':
    res = add(1,2)
    print("模块的名称_name_是%s" % __name__)