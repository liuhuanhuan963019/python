内置异常基类
在 Python 中，所有异常必须为一个派生自 BaseException 的类的实例。 通过子类化创建的两个不相关异常类永远是不等效的，既使它们具有相同的名称。

下列异常主要被用作其他异常的基类。

BaseException：  所有异常的基类

Exception（重点掌握）

所有内置的非系统退出类异常都派生自此类。 所有用户自定义异常也应当没打算自此类。

ArithmeticError

此基类用于派生针对各种算术类错误而引发的内置异常: OverflowError, ZeroDivisionError, FloatingPointError。

BufferError

当与 缓冲区 相关的操作无法执行时将被引发。

LookupError

此基类用于派生当映射或序列所使用的键或索引无效时引发的异常: IndexError, KeyError

内置异常的层次结构
BaseException             所有异常的基类         
 +-- SystemExit              解释器请求退出
 +-- KeyboardInterrupt          用户中断执行(通常是输入^C)
 +-- GeneratorExit            生成器(generator)发生异常来通知退出
 +-- Exception               常规错误的基类
      +-- StopIteration              迭代器没有更多值 
      +-- StopAsyncIteration              必须通过异步迭代器对象的__anext__()方法引发以停止迭代
      +-- ArithmeticError                 所有数值计算错误的基类
      |    +-- FloatingPointError             浮点计算错误
      |    +-- OverflowError                  数值运算超出最大限制
      |    +-- ZeroDivisionError              除(或取模)零 (所有数据类型
      +-- AssertionError                  断言语句失败
      +-- AttributeError                  对象没有这个属性
      +-- BufferError                    与缓冲区相关的操作时引发
      +-- EOFError                        没有内建输入,到达EOF 标记
      +-- ImportError                     导入失败
      |    +-- ModuleNotFoundError        找不到模块
      +-- LookupError                     无效数据查询的基类
      |    +-- IndexError                      序列中没有此索引(index)
      |    +-- KeyError                        映射中没有这个键
      +-- MemoryError                     内存溢出错误
      +-- NameError                       未声明、初始化对象
      |    +-- UnboundLocalError              访问未初始化的本地变量
      +-- OSError                         操作系统错误，
      |    +-- BlockingIOError               操作将阻塞对象设置为非阻塞操作
      |    +-- ChildProcessError             子进程上的操作失败
      |    +-- ConnectionError               与连接相关的异常的基类
      |    |    +-- BrokenPipeError             在已关闭写入的套接字上写入
      |    |    +-- ConnectionAbortedError      连接尝试被对等方中止
      |    |    +-- ConnectionRefusedError      连接尝试被对等方拒绝
      |    |    +-- ConnectionResetError        连接由对等方重置
      |    +-- FileExistsError               创建已存在的文件或目录
      |    +-- FileNotFoundError             请求不存在的文件或目录
      |    +-- InterruptedError              系统调用被输入信号中断
      |    +-- IsADirectoryError             在目录上请求文件操作
      |    +-- NotADirectoryError            在不是目录的事物上请求目录操作
      |    +-- PermissionError              在没有访问权限的情况下运行操作
      |    +-- ProcessLookupError            进程不存在
      |    +-- TimeoutError                  系统函数在系统级别超时
      +-- ReferenceError                弱引用试图访问已经垃圾回收了的对象
      +-- RuntimeError                  一般的运行时错误
      |    +-- NotImplementedError      尚未实现的方法
      |    +-- RecursionError           解释器检测到超出最大递归深度
      +-- SyntaxError                   Python 语法错误
      |    +-- IndentationError         缩进错误
      |         +-- TabError          Tab 和空格混用
      +-- SystemError              一般的解释器系统错误
      +-- TypeError               对类型无效的操作
      +-- ValueError              传入无效的参数
      |    +-- UnicodeError             Unicode 相关的错误
      |         +-- UnicodeDecodeError     Unicode 解码时的错误
      |         +-- UnicodeEncodeError     Unicode 编码时错误
      |         +-- UnicodeTranslateError  Unicode 转换时错误
      +-- Warning                       警告的基类
           +-- DeprecationWarning          关于被弃用的特征的警告
           +-- PendingDeprecationWarning   关于构造将来语义会有改变的警告
           +-- RuntimeWarning           可疑的运行行为的警告
           +-- SyntaxWarning            可疑的语法的警告
           +-- UserWarning              用户代码生成的警告
           +-- FutureWarning            有关已弃用功能的警告的基类
           +-- ImportWarning            模块导入时可能出错的警告的基类
           +-- UnicodeWarning           与Unicode相关的警告的基类
           +-- BytesWarning             bytes和bytearray相关的警告的基类
           +-- ResourceWarning           与资源使用相关的警告的基类。。