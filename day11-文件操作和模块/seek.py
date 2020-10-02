'''
    seek()  定位到文件的其他地方进行操作
    seek(offset,from) 有2个参数，offset,偏移量单位字节，负数是往回偏移，正数是往后偏移，from位置，
    0表示文件开头，1表示当前位置，2表示文件，末尾
'''
with open("文件操作笔记.md","rb") as fp:
    data = fp.read(9)
    print(data.decode("utf-8"))
    fp.seek(-6,1)  #从当前位置向前移动9个位置  相当于重新回到文件的开头位置
    print(fp.read(9).decode("utf-8"))   #输出相同的文件
    print(fp.read().decode('utf-8'))
    fp.seek(-9,2)  #从文件末尾向前移动8个位置
    print(fp.read(9).decode("utf-8"))
    #对于这种情况，用'r'这种模式打开文件，在文本文件中，没有使用二进制的选项打开文件，
    # 只允许从文件的开头计算相对位置，从文件尾部计算或者当前计算的话就会引起异常





