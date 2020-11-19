import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

#method 1 subplot2grid
# plt.figure()
# #(3,3)表示整个网格大小，（0，0)表示起始列表，colspan=3 表示跨度3行，rowspan表示跨度为1列
# ax1 = plt.subplot2grid((3,3),(0,0),colspan=3,rowspan=1)
# ax1.plot([1,2],[1,2])
# #设置某个指定的x轴标题名称
# ax1.set_xlabel("x")
# ax1.set_title("ax1_title")
#
# ax2 = plt.subplot2grid((3,3),(1,0),colspan=2,rowspan=1)
# ax2.plot([1,2],[1,2])
# #设置某个指定的x轴标题名称
# ax2.set_xlabel("x")
# ax2.set_title("ax2_title")
# ax3 = plt.subplot2grid((3,3),(1,2),colspan=1,rowspan=2)
# ax4  = plt.subplot2grid((3,3),(2,0))
# ax5  = plt.subplot2grid((3,3),(2,1))
# ax6  = plt.subplot2grid((3,3),(2,2))


#method2  gridspec
# plt.figure()
# gs = gridspec.GridSpec(3,3)
# ax1 = plt.subplot2grid(gs[0,:])
# ax2 = plt.subplot2grid(gs[1,:2])
# ax3 = plt.subplot2grid(gs[1:,2])
# ax4 = plt.subplot2grid(gs[-1,0])
# ax5 = plt.subplot2grid(gs[-1,-2])


#methpd 3  sharex=True,sharey=True表示共享x,y轴
f,((ax11,ax12),(ax21,ax22))=plt.subplots(2,2,sharex=True,sharey=True)
ax11.scatter([1,1],[1,1])
plt.show()