#Review E field physics problems

import numpy as np
import matplotlib.pyplot as mpl
# extend these boundaries and update the 0 matrix to reflect that
xlist = np.arange(-5,5,0.01)
ylist = np.arange(-5,5,0.01)
i = 0
# q = 1 #for a charge not at the origin
# k = 1 #for a charge not at the origin
Ex = np.zeros((len(xlist),len(xlist))) #len(xlist)
Ey = np.zeros((len(ylist),len(ylist))) #len(ylist)
for x in xlist:
    j = 0
    for y in ylist:
        #point Q1(-10,-10) and Q2(1,1)
        Ex[j,i] = ((x+10)/(np.sqrt((x+10)**2+(y+10)**2)**3) +
                   (x-1)/(np.sqrt((x-1)**2+(y-1)**2)**3))# add x comp of other charge
        Ey[j,i] = ((y+10)/(np.sqrt((x+10)**2+(y+10)**2)**3) +
                   (y-1)/(np.sqrt((x-1)**2+(y-1)**2)**3))# add y comp of other charge
        j = j+1
    i = i+1
mpl.streamplot(xlist,ylist,Ex,Ey,5)
#mpl.streamplot(xlist,ylist,Ey,Ex)
mpl.show()
# plt.quiver(xlist,ylist,Ey,Ex)
# Homework make for 2 point charges
# q = 1 at (1,0)
# q = 1 at (-1,0)
# review electric field charges 
