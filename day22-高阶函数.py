import numpy

# map
# def f(x):
#     return x*x
#
#
# a = map(f,[1,3,4,5,6])
# print(list(a))


# filter()

def odd(n):
    if n%2==0:
        return True
    else:
        return False

# 过滤出只有偶数的数
r = list(filter(odd,[1,2,3,4,5,6,7]))
print(r)