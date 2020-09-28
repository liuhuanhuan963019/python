#encoding = utf-8
'''
    递归，自己调用自己
    必须要有一个明确的结束条件
    优点：逻辑简单，定义简单
    缺点：容易导致栈溢出，内存资源紧张，甚至内存溢出
'''

#求阶乘
#普通方法
# def jc(n):
#     s = 1
#     for i in range(1,n+1):
#         s *= i
#         pass
#     return s
#     pass

#递归方式
# s=1
# def dg(n):
#     '''
#     递归实现参数的调用
#     :param n:
#     :return:
#     '''
#     if n == 1:
#         return 1
#         pass
#     else:
#         return n*dg(n-1)
#         pass
#     pass
# print(dg(4))


#递归案例  模拟实现树形结构的遍历
import os   #引入文件的操作模块
def findFile(file_path):
    listRs = os.listdir(file_path)  #列出该路径下面所有的文件夹
    for fileItem in listRs:
        full_path = os.path.join(file_path,fileItem) #获取完整的文件路径
        if os.path.isdir(full_path): #判断是否是个文件夹
            findFile(full_path)  #如果是文件夹就递归去找文件
        else:
            print(fileItem)
            pass
        pass
    else:
        return
    pass

findFile("/Users/liuhuanhuan/Documents/ArcGIS")
