#xlist, ylist array from -10,10, 0.01
# 4
import numpy as np
import matplotlib.pyplot as mpl

xlist = np.arange(-100,100,1)
ylist = np.arange(-100,100,1)
# print(xlist.size)
i = 0
q = 1
k = 10*6
Ex = np.zeros((200,200)) #len(xlist)
Ey = np.zeros((200,200)) #len(ylist)
for x in xlist:
    j = 0
    for y in ylist:   
        Ex[j,i] = k*q*(x/(np.sqrt(x**2+y**2)**3) + (x+1)/(np.sqrt((x+1)**2+(y+1)**2)**3))
        Ey[j,i] = k*q*(y/(np.sqrt(x**2+y**2)**3) + (y+1)/(np.sqrt((x+1)**2+(y+1)**2)**3))
        j = j+1
    i = i+1   
mpl.streamplot(xlist,ylist,Ex,Ey,5)
#mpl.streamplot(xlist,ylist,Ey,Ex)
mpl.show()
# plt.quiver(xlist,ylist,Ey,Ex)

