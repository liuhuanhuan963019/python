import modeTest   #导入模块  第一种导入方式
# # from modeTest import add  #第二种
# # from modeTest import *   #第三种
# re = modeTest.add(1,2)   #模块中的测试代码也被执行了  如果想要测试的代码不执行就需要加上一个判断（见原模块中）
# print(re)
# print(modeTest.diff(3,4))
# #此时的 运行结果中就不包含测试中的代码
print(modeTest.printInfo())   #使用第一种方式引入模块则即使不在__all__函数中也可以执行

#使用此方式引入模块，若模块中有__all__函数，则引用的函数均来自于__all__函数中
# from modeTest import *
# print(add(1,2))
# print(diff(1,2))
# # print(printInfo())   #此时这个函数无法调用成功，因为在模块中__all__中未定义引用此方法





