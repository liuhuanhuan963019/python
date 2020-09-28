#encoding=utf-8

'''
    人物：西门吹雪  叶孤城
    name   玩家名称
    blood  玩家血量

    方法：
    tong() 捅对方一刀，对方掉10滴
    kanren() 砍对方一刀，对方掉15滴
    chiyao() 吃一颗药，回10滴
    _str_  打印玩家状态
'''
import time
class Role:

    def __init__(self,name,blood):
        '''
        初始化对象
        :param name: 姓名
        :param blood: 血量
        '''
        self.name = name
        self.blood = blood
        pass

    def tong(self,enemy):
        '''
        self 捅了enemy一刀减了10滴血
        :param enemy:  敌人
        :return:
        '''
        enemy.blood -= 10
        print("%s 捅了 %s 一刀 掉了10滴血" % (self.name, enemy.name))
        pass

    def kanren(self,enemy):
        '''
        self 砍了enemy一刀减了15滴血
        :param enemy: 敌人
        :return:
        '''
        enemy.blood -= 15
        print("%s 砍了 %s 一刀 掉了15滴血" % (self.name,enemy.name))
        pass

    def chiyao(self):
        '''
        回血
        :return:
        '''
        self.blood += 10
        print("%s吃了口药回了10滴血" % self.name)
        pass

    def __str__(self):
        return "%s玩家 当前剩余血量%d" % (self.name,self.blood)
        pass


#实例化对象
ximen = Role("西门吹雪",100)
gc = Role("叶孤城",100)
ximen.tong(gc)
print(gc)
gc.kanren(ximen)
print(ximen)

ximen = Role("西门吹雪", 100)
gc = Role("叶孤城", 100)
while True:
    if ximen.blood <= 0 or gc.blood <= 0:
        break
        pass
    ximen.tong(gc)
    print(gc)
    gc.kanren(ximen)
    print(ximen)
    time.sleep(1)

print("游戏结束")


