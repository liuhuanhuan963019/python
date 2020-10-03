import sys
# sys.getrefcount()
a = []
print(sys.getrefcount(a))    #两次  sys.getrefcount 执行完毕之后那一次就会自动剪掉
b=a
print(sys.getrefcount(a))    #三次
d=b
f=d
e=f
print(sys.getrefcount(a))   #6次