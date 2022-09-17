#xlist, ylist array from -10,10, 0.01
import numpy as np
import matplotlib.pyplot as mpl

xlist = np.arange(-5,5,0.1)
ylist = np.arange(-5,5,0.1)
i = 0
q = 1
k = 1
Ex = np.zeros((100,100)) #len(xlist)
Ey = np.zeros((100,100)) #len(ylist)
for x in xlist:
    j = 0
    for y in ylist:   
        Ex[j,i] = x/(np.sqrt(x**2+y**2)**3) + (x+1)/(np.sqrt((x+1)**2+(y+1)**2)**3)
        Ey[j,i] = y/(np.sqrt(x**2+y**2)**3) + (y+1)/(np.sqrt((x+1)**2+(y+1)**2)**3)
        j = j+1
    i = i+1
mpl.streamplot(xlist,ylist,Ex,Ey,5)
#mpl.streamplot(xlist,ylist,Ey,Ex)
mpl.show()
# plt.quiver(xlist,ylist,Ey,Ex)
