1。引用计数机制
2。python中的循环数据结构及引用计数
3。python中的GC模块
4。python 内存优化
5。python pep8规范
6。python命令行参数



### 引用计数机制模型：

​				python里每一个东西都是对象，它们的核心是一个结构体：P yobject

​		

``` c
typedef struct object{
		int ob_refcnt;
  	struct_typeobject *ob_type;
}Pyobject;
```

​					PyObject是每个对象必有的内容，其中ob_refcnt就是做为引用计数。当一个对象有新的引用时，它的obrefcnt就会增加，当引用它的对象被删除，它的o b_refcnt就会减少

​	

```c++
#define Py_INCREF(op)
if （--(op)->ob_refcnt !=0)
  	;
else
  	_Py_Dealloc((PyObject*)(op))
```

当引用计数为0时，该对象生命就结束了	

![image-20201004005014248](/Users/liuhuanhuan/Library/Application Support/typora-user-images/image-20201004005014248.png)

#### 引用计数优点：

​	1.简单

​	2.实时性：一旦没有引用，内存就直接释放了。不用像其他机制需要等到特定时机，实时性还带来一个好处：处理回收内存的事件分摊到平时

#### 引用计数缺点：

​	1.维护引用计数会消耗资源

​	2.循环引用

​		

```
list1 = []
list2 = []
list1.append(list2)
list2.append(list1)
```

​	list1 和list2相互引用，如果不存在其他对象对它们的引用，list1和lis t2的引用计数也仍然为1，所占用的内存永远无法被回收，这是致命的

​	python仍将引入新的回收机制（标记清除和分代收集）