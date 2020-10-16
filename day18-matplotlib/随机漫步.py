import matplotlib.pyplot as plt
from random import choice
'''
    随机漫步：每次行走都是完全随机的，没有明确的方向，结果是由一系列随机决策决定的
    
'''

class RandomWalk():
    '''
        一个随机漫步的类
    '''
    def __init__(self,num_points = 5000):
        self.num_points = num_points
        
        #所有的漫步随机都始于（0，0）
        self.x_values = 0
        self.y_vlaues = 0
    
    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            
            #决定前进方向以及沿这个方向前进的距离
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = x_direction * x_distance
            
            #拒绝原地
            if x_step == 0 and y_step == 0:
                continue

            #计算下一个点的x和y的值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)


rw = RandomWalk()
rw.fill_walk()
plt.scatter(rw.x_values,rw.y_vlaues,s=15)
plt.show()