'''
    tell()
        文件定位：指的是当前文件指针读取到的位置，光标位置，在读写文件的过程中，如果想知道文件的位置
        可以用tell来获取当前文件的位置
'''
#一个utf-8中文占三为，gbk占两位
with open("文件操作笔记.md","r") as read_f:
    print(read_f.read(3))  #读取三个字符
    print(read_f.tell())   #此时为当前光标所在位置
    print(read_f.read(2))
    print(read_f.tell())