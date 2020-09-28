#encoding=utf-8

'''
    all()
    any()
    sorted()
    reverse()
    range()
    zip()
    enumerate()
'''
#[]列表  ()元组   {}字典
#all 函数用于判断给定的元组或列表中所有元素是否都为true，如果是，返回true,否则，返回false元素
#除了0。空。false，外都算true
'''
    空列表和空元组返回true
    函数等价于:
        def all(iterable):
            for element in iterable:
                if not element:
                    return false
            return true
'''

li = [1,2,3]
print(all(li))  #true

li = [1,2,3,False]
print(all(li))  #false



'''
    any() 判断给定的参数是否全部为false,则返回false，有一个为true则返回true
    元素除了0，flase,空以外都算true
    类似于逻辑运算符中的or
'''
print(any([1,2,3,4,0])) #true



