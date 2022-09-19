import numpy as np
import matplotlib.pyplot as plt

xlist = np.arange(-5,5,0.1)
ylist = np.arange(-5,5,0.1)

X,Y = np.meshgrid(xlist,ylist)
# X a 2D array of 10,000 numbers np.size(xlist)
# Y a 2D array of 10,000 numbers np.size(ylist)
# to get the (size,size) matrix use np.size(X)

k = 1
q = 10 ** -6

Ex = k * q * X / (np.sqrt(X ** 2.0 + Y ** 2.0) ** 3.0)
Ey = k * q * Y / (np.sqrt(X ** 2.0 + Y** 2.0) ** 3.0) 

plt.streamplot(X,Y,Ex,Ey)
plt.show()