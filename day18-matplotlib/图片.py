import numpy as np
import matplotlib.pyplot as plt

a = np.array([0.313,0.365,0.423,0.363,0.439,0.525,0.423,0.525,0.651]).reshape(3,3)

#显示图片
plt.imshow(a,interpolation='nearest',cmap='bone',origin='upper')
plt.colorbar(shrink=0.9)


plt.xticks(())
plt.yticks(())
plt.show()