'''
    os模块：
        对文件进行重命名、删除等一系列操作，在python中可以利用os模块
    os模块提供了一些系统级别的操作
    import os
    修改文件名：rename(需要修改的文件名，新的文件名)
        os.rename('1.py','2.py')
    删除文件:remove（待删除的文件名）
        os.remove('3.py')
    创建文件夹：mkdir(文件夹名称)
        os.mkdir('gl')
    删除文件夹:rmdir(文件夹名称)
        os.rmdir('gl')
    获取当前目录：getcwd()
        os.getcwd()
    切换目录：chdir(路径)
        os.chdir('../')
    路径拼接：os.path.join(path1[,path2[]])  将多个路径组和到一起，返回
        path = os.path.join(os.getcwd(),'gl')
    列表方式打印：
        os.listdir("dname")
'''
import os
import shutil
# os.rename('text01.txt','demo01.txt')
# os.remove('text02.txt')

#可以创建单级目录
# os.mkdir("/Users/liuhuanhuan/Downloads/idea")
# os.rmdir("/Users/liuhuanhuan/Downloads/idea")  #删除文件夹

##可以创建多级目录
# os.makedirs("/Users/liuhuanhuan/Downloads/idea/l/h/h/w/c/y/wo/ai/ni")  #允许创建多级目录
# os.rmdir("/Users/liuhuanhuan/Downloads/idea")  #删除失败。只能删除目录文件下面是空的

#如果要删除非空目录的话，就需要调用shutil模块
# shutil.rmtree("/Users/liuhuanhuan/Downloads/idea")  #成功删除非空的文件夹

#获取当前的目录
# print(os.getcwd())

#路径的拼接
# print(os.path.join(os.getcwd(),'venv'))

#获取文件目录的列表
#原始版本的写法
# listRs = os.listdir('/Users/liuhuanhuan/')
# for name in listRs:
#     print(name)   #打印列表的名称

#使用新型写法 (可以实现如上功能)
# with os.scandir("/Users/liuhuanhuan/") as entries:  #使用with自动的去释放资源
#         for entry in entries:
#             print(entry.name)
#             pass

#示范:查看一个文件夹下所有的文件
basePath = "/Users/liuhuanhuan/"
for entry in os.listdir(basePath):
    # if os.path.isfile(os.path.join(basePath,entry)):   #只显示是文件的目录文件名称
    #     print(entry)
    if os.path.isdir(os.path.join(basePath,entry)):   #只显示是文件夹的目录名称 
        print(entry)
        pass



