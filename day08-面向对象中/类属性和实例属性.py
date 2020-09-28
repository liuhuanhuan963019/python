#类属性就是类对象所拥有的属性
#类对象可以由类属性和实例属性共同访问  而实例属性只可以由实例对象访问
class Student:
    name = "hah"  #属于类属性，就是Student所拥有的属性
    def __init__(self,age):
        self.age = age   #实例属性
        pass
    pass

stu = Student(10)
print("%s今年%d" % (stu.name,stu.age))  #通过实例对象访问类属性
# stu.name = "lhh"  #此操作无法实现，应为类属性只属于类对象，只能通过类对象来修改
Student.name = "lhh"
print("..........................通过类对象访问类属性")

print(Student.name)
# print(Student.age)   报错  只有类对象才能直接访问类属性，不可直接访问实例属性
