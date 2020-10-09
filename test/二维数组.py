#encoding=utf-8
import numpy as nu

#二维数组详细介绍:https://blog.csdn.net/weixin_43542202/article/details/107977584?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param
'''
#普通定义方式 义list的方式直接定义一个二维数组
li = [[1,2],[21,2]]
for item in li:
    for i in item:
        print(i)
'''

'''
    numpy中的array定义二维数组
    Python中采用独立的"[ ]"而非（）来表示元素的索引。
'''
group = [[9,2],[3,4],[5,6]]
group2 = nu.array([[1,2,3],[4,5,6]])
# print(group2)
# print(group)
print(group[1])
print(group2[1])
'''
    [3, 4]
    [4 5 6]    
'''

#求最大最小值
print(max(group))    #[5, 6]  计算没一列的最大值
print(max(max(group)))   #可以得到整个数组中的最大的元素

print(nu.max(group2))    #可以得到数组中的最大元素

'''
    Python中的list是python的内置数据类型，list中的数据类不必相同的。
    在list中的数据类型保存的是数据所存放的地址，简单的说就是指针，并非数据。
    而Numpy中的array所存放的数据类型必须全部相同。
    因此，在求最大最小值的时候，我们可以简记为Numpy数组必须用Numpy操作。
'''





