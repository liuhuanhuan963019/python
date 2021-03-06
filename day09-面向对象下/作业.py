#1.python中new方法的作用是什么
#用来创建实例对象，只有继承object的话，才能有这个方法

#2.什么是单例模式？单例模式适用于什么场景
#要求一个类只能有一个实例，并且提供一个全局的访问点
#场景：日志记录、网站计数器、权限验证、window资源管理器、系统回收站、数据库连接

#3.私有化方法和私有化属性在子类中能够继承
#不能

#4.在python中什么是异常
#异常就是程序执行过程中发生的错误

#5.python中是如何处理异常的
#根据异常的类型去处理

#6.异常处理的格式
# try:
#                 可能会出错的代码
#             except:
#                 出错后执行的代码
#             else:
#                 没有出错的代码
#             finally:
#                 不管有没有出错都执行的的代码

#7._slots_作用
#限制属性的输入  节约内存空间

#8.私有化属性的作用
#保护数据，封装的表现

#9.在类的外面是否可以直接修改私有属性
#不可以直接修改，必须要通过方法去实现

#10.如果一个类中，只有指定的属性和方法能被外部修改，那么该如何限制外部修改
#对属性进行私有化设定
