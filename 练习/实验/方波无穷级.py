'''
利用numpy和matplotlib在坐标系中绘制方波的无穷级数表示。方波无穷级数表达式为：emm百度

'''

import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 1000)
y=0
for k in range(1, 10, 1):
    y=y+4*np.sin((2*k-1)*x)/((2*k-1)*np.pi)
plt.plot(x,y,'k',color='r',label="w=1",linewidth=3)
plt.axis([0,10,-1.5,1.5])
plt.legend()
plt.show()