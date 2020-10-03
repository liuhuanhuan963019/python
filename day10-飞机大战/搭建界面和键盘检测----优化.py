import pygame   #引用第三方的库
import random   #随机产生数据的库
import time
from pygame.locals import *


'''
    1.实现飞机的显示  并且可以控制飞机的移动【面向对象】    
'''

#抽象出一个飞机的基类
class BasePlane(object):
    def __init__(self,screen,imagePath):
        '''
        初始化基类
        :param screen: 主窗体对象
        :param imageName: 加载的图片
        '''
        self.screen = screen
        self.image = pygame.image.load(imagePath)
        self.bulletList = []   #存储所有的子弹

    def display(self):
        '''
                在主窗口中显示飞机
                :return:
                '''
        self.screen.blit(self.image, (self.x, self.y))

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

'''
    公共的子弹类
'''
class commonBullet(object):
    def __init__(self,x,y,screen,bulletType):
        self.type = bulletType
        self.screen = screen
        if self.type == 'hero':
            self.x += 13
            self.y -= 20
            self.imagePath = 'drhDe29TEts.jpg'
            pass
        elif self.type == 'enemy':
            self.x += 13
            self.y -= 20
            self.imagePath = 'drhDe29TEts.jpg'
            pass
        self.image = pygame.image.load(self.imagePath)
        pass

    def move(self):
        '''
        子弹的移动
        :return:
        '''
        if self.type == 'hero':
            self.y -= 2
        elif self.type == 'enemy':
            self.y += 2
        pass
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        pass
    def judge(self):
        '''
        判断子弹是否越界
        :return:
        '''
        if self.y > 500 or self.y < 0:
            return True
        else:
            return False

    pass
class HeroPlane(BasePlane):
    def __init__(self,screen):
        '''
        初始化函数
        :param screen: 主窗体对象
        '''
        #飞机的默认位置
        super().__init__(screen,'drhDe29TEts.jpg')  #调用父类的方法
        self.x = 150
        self.y = 450
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
    #发射子弹
    def sheBullet(self):
        #创建一个新的子弹对象
        newBullet = commonBullet(self.x,self.y,self.screen,'hero')
        self.bulletList.append(newBullet)
        pass
    pass



'''
    创建一个敌机类    
'''
class  EnemyPlane(BasePlane):
    def __init__(self,screen):
        super().__init__(screen,'drhDe29TEts.jpg')   #需要修改的地址
        #默认的一个方向
        self.direction = 'right'
        #飞机的默认位置
        self.x = 0
        self.y = 0
        pass


    def sheBuller(self):
        '''
        敌机随机的发射子弹
        :return:
        '''
        num = random.randint(1,50)
        if num == 3:
            newBullet = commonBullet(self.x,self.y,self.screen,'enemy')
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