#xlist, ylist array from -10,10, 0.01
import numpy as np
import matplotlib.pyplot as mpl

xlist = np.arange(-10,10,0.1)
ylist = np.arange(-10,10,0.1)
# to check size
# print(ylist.size)

i = 0
q = 1
k = 1
Ex = np.zeros((200,200)) #len(xlist)
Ey = np.zeros((200,200)) #len(ylist)
for x in xlist:
    j = 0
    for y in ylist:   
        Ex[j,i] = x/(np.sqrt(x**2+y**2)**3) # add x comp of other charge
        Ey[j,i] = y/(np.sqrt(x**2+y**2)**3) # to y comp of everything 
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


