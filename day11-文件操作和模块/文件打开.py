'''
    文件的操作：
        打开：open
'''
#'w'用于写的操作，如果文件已经存在，则将其覆盖掉，如果文件不存在，就创建新的文件
# #默认的编码格式是gbk的格式，这个是中文编码，最好的是我们打开一个文件的时候，就给它指定一个编码类型
# fobj = open('./文件操作笔记.md','w',encoding="utf-8")
# # fobj.write("我想你了")
# fobj.write("wo dani d lian")
#
# fobj.close()


#以二进制的形式去打开文件
# fobj = open("./文件操作笔记.md","wb") #str->bytes
# fobj.write("在这个与那个之间的函数啊".encode('utf-8'))   #指定编码格式用于字节流的文件读写
# fobj.close()


#以a的方式打开文件
# fobj = open("./文件操作笔记.md","a") #str->bytes
# fobj.write("在这个与那个之间的函数啊,二狗子，我想你了")   #指定编码格式用于字节流的文件读写
# fobj.close()

#以ab的方式打开文件  在文件末尾追加一段数据
fobj = open("./文件操作笔记.md","ab") #用于在文件末尾追加数据
fobj.write("在这个与那个之间的函数啊,二狗子，我想你了\r\n".encode('utf-8'))   #指定编码格式用于字节流的文件读写
fobj.write("在这个与那个之间的函数啊,二狗子，我想你了\r\n".encode('utf-8'))   #指定编码格式用于字节流的文件读写
fobj.close()