import matplotlib.pyplot as plt
import numpy as np
import math # need math module for trigonometric functions

g = 9.81 #gravitational constant
dt = 1e-3 #integration time step (delta t)
v0 = 40 # initial speed at t = 0

angle = math.pi/4 #math.pi = 3.14, launch angle in radians

time = np.arange(0, 10, dt) #time axis
vx0 = math.cos(angle)*v0 # starting velocity along x axis
vy0 = math.sin(angle)*v0 # starting velocity along y axis

xa = vx0*time # compute x coordinates
ya = -0.5*g*time**2 + vy0*time # compute y coordinates

def traj_fric(angle, v0): # function for trajectory

    vx0 = math.cos(angle) * v0 # for some launch angle and starting velocity
    vy0 = math.sin(angle) * v0 # compute x and y component of starting velocity

    x = np.zeros(len(time))   #initialise x and y arrays
    y = np.zeros(len(time))

    x[0], y[0], 0 #projecitle starts at 0,0
    x[1], y[1] = x[0] + vx0 * dt, y[0] + vy0 * dt # second elements of x and
                                              # y are determined by initial 
                                              # velocity
    i = 1
    while y[i] >= 0: # conditional loop continuous until
    # projectile hits ground
        gamma = 0.005 # constant of friction
        height = 100 # height at which air friction disappears
        f = 0.5 * gamma * (height - y[i]) * dt
        x[i + 1] = (2 * x[i] - x[i - 1] + f * x[i - 1])/1 + f # numerical integration to find x[i + 1]                                       
        y[i + 1] = (2 * y[i] - y[i - 1] + f * y[i - 1] - g * dt ** 2)/ 1 + f # and y[i + 1]

        i = i + 1 # increment i for next loop

    x = x[0:i+1] # truncate x and y arrays                                                
    y = y[0:i+1]
    return x, y, (dt*i), x[i] # return x, y, flight time, range of projectile

x, y, duration, distance = traj_fric(angle, v0)

fig1 = plt.figure()
plt.plot(xa, ya) # plot y versus x
plt.xlabel ("x")
plt.ylabel ("y")
plt.ylim(0, max(ya)+max(ya)*0.2)
plt.xlim(0, distance+distance*0.1)
plt.show()

print "Distance:" ,distance
print "Duration:" ,duration

n = 5
angles = np.linspace(0, math.pi/2, n)
maxrange = np.zeros(n)

for i in range(n):
    x,y, duration, maxrange [i] = traj_fric(angles[i], v0)

angles = angles/2/math.pi*360 #convert rad to degress

print "Optimum angle:", angles[np.where(maxrange==np.max(maxrange))]
