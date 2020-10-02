class People:
    def __init__(self):
        self.__age = 18
        pass

    # def get_age(self):
    #     return self.__age
    #     pass
    # def set_age(self,age):
    #     if age < 0:
    #         print("年龄不能为负数")
    #         pass
    #     else:
    #         self.__age = age
    #         pass
    #     pass
    #定义一个类属性，可以通过类属性的形式去访问私有属性
    # age = property(get_age,set_age)


    #方法2：通过修饰器的方式来实现
    @property    #用装饰器添加属性，提供来一个getter的方法
    def age(self):
        return self.__age
    @age.setter   #提供了一个sette的方法
    def age(self,age):
        if age < 0:
            print("error")
        else:
            self.__age = age
            pass
        pass
    pass

one =People()
print(one.age)   #此时的age就相当于函数的名称
one.age = 20
print(one.age)

