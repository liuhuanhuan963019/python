#encoding=utf-8

#在函数体内  参数关键字类型只能是字典类型   key是一个字符串
def getNumber(**kwargs):
    print(kwargs)
    pass

# getNumber(1,2,34)   #不可传递


dictA = {"name":"huanhuan","id":20}
# getNumber(dictA)    不可直接传递
# getNumber(**dictA)   #可用
# getNumber(name="huanhuan",id=20)  #可用
# getNumber()    #不传为空


#组合使用 自动识别 自动填充
def complexFunc(*args,**kwargs):
    print(args)
    print(kwargs)
    pass

# complexFunc(1,2,3,4)  #输出（1，2，3，4） {}
complexFunc(1,2,3,name="huanhuan")  #输出{1,2,3} {'name':'huanhuan'}
complexFunc(age=10)


#
# def TestMup(**kwargs,*args):#不符合要求
#         '''
#         可选参数必须放到关键字可选参数当后面
#         可选参数：接受的数据是一个元组类型
#         关键字可选参数：接受的数据是一个字段类型
#         :param kwargs:
#         :param args:
#         :return:
#         '''


