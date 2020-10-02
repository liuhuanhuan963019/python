'''
    异常处理：
        格式：
            try:
                可能会出错的代码
            except:
                出错后执行的代码
            else:
                没有出错的代码
            finally:
                不管有没有出错都执行的的代码
'''
#except根据错误的具体类型来捕获的
#exception 捕获所有的异常



try:
    # print(b)
    a = [1,2,3]
    print(a[10])
    pass
except NameError as msg:
    print(msg)   #打印错误
except IndexError as msg:
    print(msg)   #输出和打印是很重要的

#不需要在所有的地方都去捕获，只要在合适的地方去捕获就可以了。这样就大大减少了写try的except

def A(s):
    return  10/int(s)
def B(s):
    return A(s)*2
def main():
    try:
        A('0')
        pass
    except Exception as msg:
        print(msg)
        pass
    pass
main()


print("try——except-else........................")
try:
    print('aa')
    pass
except Exception as msg:
    print(msg)
    pass
else:
    print("没有错我才会执行的呢")
finally:  #通常用于释放文件资源和数据库连接等方面才可以用到
    print("不管咋样我都执行")