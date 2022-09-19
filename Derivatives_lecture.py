import numpy as np
# limit definition of derivative
# the derivative is the slope of the tangent line at a point x_0,f(x_0)
# How do we numerically calculate the derivative of a function with a computer?
# create a derivative, see what is the most accureate between
# forward method, backwards method, or center method
# define a function

# central difference method:
# average the forward and backward difference method

#forward difference method
def deriv_sin_fwd(x,h=0.01):
    return(np.sin(x+h) - np.sin(x)) / h
#backwards difference method
def deriv_sin_bck(x,h=0.01):
    return(np.sin(x) - np.sin(x-h)) / h
def deriv_sin_fun(x,h=0.01):
    return(np.sin(x+h)-f(x-h)) / 2h
        
print(deriv_sin(np.pi))
print(deriv_sin(0))
print(deriv_sin(np.pi/3))

#this is called the finite difference method, using finite numbers in the difference quotient.
# the central difference method is to find a slope by combining the forward and backwards method
print(deriv_sin(np.pi/3,0.000000000001)) # optimum difference
