# fp = open("文件操作笔记.md","r")
# content = fp.read()
# print(content)
# fp3 = open("文件操作笔记_备份.md","w")
# fp3.write(content)
# fp.close()
# fp3.close()


print("文件截取...................")
fp2 = open("文件操作笔记.md","r+")
fp2.truncate(9)   #将原文件全部删除，只保留前10个字符
print(fp2.read())
fp2.close()

