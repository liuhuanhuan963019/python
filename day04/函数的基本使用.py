#encoding=utf-8
'''
    def 函数名：
        代码块【一些列的代码】,
    def 函数名(int a,int b=10) 默认参数的值只能在最后面的位置
    缺省函数默认参数，
'''

# def printInfo(index):
#     print('name=%s' % 'liuhuanhuan')
#     print('age=%d' % index)
#     print('address=%s' % 'lianshui')
#     print('weight=%s' % 80)
#
# printInfo(90)


#函数返回一个字典类型
def build_person(first_name,last_name,age = ''):
    "返回一个字典类型的数据，其中包含一个人的信息"
    person = {'first':first_name,'last':last_name}
    if age:
        person['age'] = age
    return person

person = build_person('lhh','wcy',12)
print(person)


#函数结合while使用
# def get_formatted_name(first_name,last_name):
#     full_name = first_name + ' ' + last_name
#     return full_name
#
# flag = True
# while flag:
#     first_name = input('please input a name:')
#     last_name = input('please input an other name:')
#     full_name = get_formatted_name(first_name,last_name)
#     print('hello ' + full_name+'!')
#     if first_name == 'lhh':
#         flag = False


#传递一个列表
def greet_users(names):
    for name in names:
        msg = "Hello," + name.title() + "!"
        print(msg)

greet_users(['lhh','wcy','try'])


#模拟3D打印 (类似于逆序打印一样的)
unprinted_designs = ['lhh','wcy','woaini']
completed_models = []

while unprinted_designs:
    current_designs = unprinted_designs.pop()

    print("current_designs:",current_designs)
    completed_models.append(current_designs)

for completed_designs in completed_models:
    print('completed_designs:',completed_designs)


#禁止函数修改列表

#切片表示法[:]创建列表的副本。在print_models.py中，如果不想清空
#未打印的设计列表，可想如下调用
# print_models(unprinted_designs[:],completed_models)



#传递多个参数 无论多少个数据，什么类型，均可以
def make_pizza(*args):
    if args:
        for item in args:
            print(str(item) + '')

make_pizza('1','2','3')

