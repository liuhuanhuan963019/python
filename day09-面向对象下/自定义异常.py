'''
    自定义异常：
        自定义异常，都要直接或间接继承error或Exception类
        由开发者主动抛出自定义异常，在python中使用raise关键字
'''
class ToollongMyException(Exception):
    def __init__(self,len):
        '''

        :param len: 长度
        '''
        self.len = len
        pass

    def __str__(self):
        return "输入的文字长度是" + str(self.len)+"超过了默认的长度"
    pass

def name_Test():
    name = input("please input a name:")
    try:
        if len(name) > 5:
            raise ToollongMyException(len(name))
        else:
            print(name)
            pass
    except ToollongMyException as msg:
        print(msg)
        pass
    finally:
        print("执行完毕")
    pass
name_Test()