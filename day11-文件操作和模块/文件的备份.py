# def copyFile():
#     #接收读取的文件名称
#     fileName = input("please input a file name:")
#     file_list = fileName.split(".") #以.来分割文件名称
#     #构建新的文件名称
#     new_file_name = file_list[0]+"_备份"+file_list[1]
#     open_f = open(fileName,"r")  #以r形式打开文件
#     write_f = open(new_file_name,"w") #以w的形式写入
#     content = open_f.read()   #一次性将所有的文件全部读取出来，然后写入到文件中
#     write_f.write(content) #一次性全部写入到文件中，十分的消耗资源
#     open_f.close()
#     write_f.close()
#     pass
#
# copyFile()


#文件备份方案优化
def copyNewFile():
    #接收读取的文件名称
    fileName = input("please input a file name:")
    file_list = fileName.split(".") #以.来分割文件名称
    #构建新的文件名称
    new_file_name = file_list[0] + "_备份" + file_list[1]
    #新的方式优化，一次性的读取1024个字节，循环读取，使用with，节约内存空间
    try:
        with open(fileName,"r") as old_f,open(new_file_name,"w") as new_f:
            #循环读取
            while True:
                content = old_f.read(1024)
                new_f.write(content)
                if len(content) < 1024:
                    break
    except Exception as msg:
        print(msg)
    pass

copyNewFile()
