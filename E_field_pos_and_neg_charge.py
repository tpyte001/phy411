#Finished Efield from lecture with a negative and a positive charge.
import numpy as np
#create a derivative, see what is the most accureate between
# forward method, backwards method, or center method

import matplotlib.pyplot as mpl

xlist = np.arange(-5,5,0.1)
ylist = np.arange(-5,5,0.1)
# print(xlist.size())

i = 0
q = 10 ** -6
k = 1
Ex = np.zeros((100,100)) #xlist.size()  
Ey = np.zeros((100,100)) #ylist.size()
for x in xlist:
    j = 0
    for y in ylist:   
        Ex[j,i] = (-q * x/(np.sqrt(x**2+y**2)**3) + q * (x+1)/(np.sqrt((x+1)**2+(y+1)**2)**3))
        Ey[j,i] = (-q * y/(np.sqrt(x**2+y**2)**3) + q * (y+1)/(np.sqrt((x+1)**2+(y+1)**2)**3))
        j = j+1
    i = i+1
mpl.streamplot(xlist,ylist,Ex,Ey,2,linewidth=1)

mpl.show()

# plt.quiver(xlist,ylist,Ey,Ex)
