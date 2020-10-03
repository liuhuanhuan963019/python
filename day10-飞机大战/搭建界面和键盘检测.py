import pygame   #引用第三方的库
import random   #随机产生数据的库
import time
from pygame.locals import *


'''
    1.实现飞机的显示  并且可以控制飞机的移动【面向对象】    
'''
class HeroPlane(object):
    def __init__(self,screen):
        '''
        初始化函数
        :param screen: 主窗体对象
        '''
        #飞机的默认位置
        self.x = 150
        self.y = 450
        #设置要显示内容的窗口
        self.screen = screen
        #生成飞机的图片对象
        self.imageName = 'drhDe29TEts.jpg'   #图片的地址随意改变
        self.image = pygame.image.load(self.imageName)
        # 存放子弹的列表
        self.bulletList = []
        pass
    def moveLeft(self):
        '''
        左移
        :return:
        '''
        if self.x > 0:
            self.x -= 10
        pass
    def moveRight(self):
        '''
        右移
        :return:
        '''
        if self.x < 310:
            self.x += 10
        pass
    def display(self):
        '''
        在主窗口中显示飞机
        :return:
        '''
        self.screen.blit(self.image,(self.x,self.y))

        #完善子弹的展示逻辑
        newDelItemList = []
        for item in self.bulletList:
            if item.judge():
                newDelItemList.append(item)
                pass
            pass

        #重新遍历一下
        for i in newDelItemList:
            self.bulletList.remove(i)
            pass
        for bullet in self.bulletList:
            bullet.display()  #显示子弹的位置
            bullet.move()  #让这个子弹进行移动，下次再移动就会看到子弹在修改后的位置了
        pass
    #发射子弹
    def sheBullet(self):
        #创建一个新的子弹对象
        newBullet = Bullet(self.x,self.y,self.screen)
        self.bulletList.append(newBullet)
        pass
    pass

'''
    创建一个子弹累
'''
class Bullet(object):
    def __init__(self,x,y,screen):
        '''

        :param x:
        :param y:
        :param screen:
        '''
        self.x = x+13
        self.y = y-20
        self.screen = screen
        self.image =  pygame.image.load('drhDe29TEts.jpg')   #子弹的路径地址需要更改
        pass

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        pass

    def move(self):
        pass

    def judge(self):
        '''
        判断子弹是否越界
        :return:
        '''
        if self.y < 0:
            return True
        else:
            return False
        pass


'''
    创建一个敌机类    
'''
class  EnemyPlane:
    def __init__(self,screen):
        #默认的一个方向
        self.direction = 'right'
        #飞机的默认位置
        self.x = 0
        self.y = 0
        #设置要显示的窗口的内容
        self.screen = screen
        self.bulletList = []
        #生成飞机的图片对象
        self.imageName = 'drhDe29TEts.jpg'
        self.image = pygame.image.load(self.imageName)
        pass
    def display(self):
        #显示敌机以及子弹位置的信息
        self.screen.blit(self.image,(self.x,self.y))
        # 完善子弹的展示逻辑
        newDelItemList = []
        for item in self.bulletList:
            if item.judge():
                newDelItemList.append(item)
                pass
            pass

        # 重新遍历一下
        for i in newDelItemList:
            self.bulletList.remove(i)
            pass
        for bullet in self.bulletList:
            bullet.display()  # 显示子弹的位置
            bullet.move()  # 让这个子弹进行移动，下次再移动就会看到子弹在修改后的位置了
        pass
        pass

    def sheBuller(self):
        '''
        敌机随机的发射子弹
        :return:
        '''
        num = random.randint(1,50)
        if num == 3:
            newBullet = EnemyBullet(self.x,self.y,self.screen)
            self.bulletList.append(newBullet)
        pass
    def move(self):
        '''
        敌机移动随机进行

        :return:
        '''
        if self.direction == 'right':
            self.x += 2
            pass
        elif self.direction == 'left':
            self.x -= 2
            pass
        if self.x > 330:
            self.direction = 'left'
            pass
        elif self.x < 0:
            self.direction = 'right'
            pass
        pass
    pass

'''
    敌机放射子弹类
'''
class EnemyBullet(object):
    def __init__(self,x,y,screen):
        '''

        :param x:
        :param y:
        :param screen:
        '''
        self.x = x
        self.y = y+10
        self.screen = screen
        self.image =  pygame.image.load('drhDe29TEts.jpg')   #子弹的路径地址需要更改
        pass

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        pass

    def move(self):
        self.y += 2
        pass

    def judge(self):
        '''
        判断子弹是否越界
        :return:
        '''
        if self.y > 500:
            return True
        else:
            return False
        pass

def key_control(HeroObj):
    '''
    定义普通的函数用来检测键盘
    :param HeroObj: 可控制检测的对象
    :return:
    '''
    # 获取键盘事件
    evenlist = pygame.event.get()
    for enevt in evenlist:
        if enevt.type == QUIT:
            print('退出')
            exit()
            pass
        elif enevt.type == KEYDOWN:
            if enevt.type == K_a or enevt.type == K_LEFT:
                print('left')
                HeroPlane.moveLeft()  # 调用函数实现左移动
                pass
            pass
        elif enevt.type == K_d or enevt.type == K_RIGHT:
            print('right')
            HeroPlane.moveRight()  # 调用函数实现右移动
            pass
        elif enevt.type == K_SPACE:
            print('按下空格键space发射子弹')
            HeroObj.sheBullet()
    pass

def main():
    #首先创建一个窗口用于显示
    screen = pygame.display.set_mode((345,500))
    #设定一个背景图像
    background = pygame.image.load('drhDe29TEts.jpg')   #背景图片地址
    #设置一个标题
    pygame.display.set_caption('打飞机')

    #设置背景音乐
    pygame.mixer.init()
    pygame.mixer.music.load('李映川 - 玫瑰.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)  #-1表示无限循环

    #载入玩家的飞机图片   更改为创建了一个飞机对象
    hero = HeroPlane(screen)   #飞机图片地址

    #创建一个敌人飞机的对象
    enemyPlane = EnemyPlane(screen)

    #设定需要显示到内容
    while True:
        screen.blit(background,(0,0))
        #显示玩家飞机的图片
        hero.display()
        enemyPlane.display()   #显示敌机
        enemyPlane.move()  #敌机移动
        enemyPlane.sheBuller()  #敌机随机发送子弹
        #获取键盘事件
        key_control(hero)
        #更新显示内容
        pygame.display.update()
        # time.sleep(1)  #休眠一秒钟
        pygame.time.Clock().tick(5)
    pass
# if __name__ == 'main':
main()