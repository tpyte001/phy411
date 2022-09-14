import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5,5,0.01)
y = np.exp(-x*x/2)/np.sqrt(2*np.pi)

plt.plot(x,y)
plt.xlabel("$x$")
plt.ylabel("$\mathcal{N}(x)$")
plt.title("Gaussian Distribution")
plt.show()