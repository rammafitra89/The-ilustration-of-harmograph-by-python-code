# create module python
import numpy as np
import matplotlib.pyplot as plt

#parameter
n = 1000000
t = np.logspace(np.log10(10),np.log10(500),n)

#we can change the paremeter
A = [  3, 6, 1.5, 1.5 ]
d = [ .004, .001, .002, .0015 ]
f = [   3, 1, 2, 2.5 ]

# create x and y
x = A[0]*np.sin(t*f[0])*np.exp(-d[0]*t) + A[1]*np.sin(t*f[1])*np.exp(-d[1]*t)
y = A[2]*np.sin(t*f[2])*np.exp(-d[2]*t) + A[3]*np.sin(t*f[3])*np.exp(-d[3]*t)

# show the plot
plt.plot(x,y,'k',linewidth=.1)
plt.axis('off')
plt.show()  # figure_1

# we can see every component
plt.plot(np.sin(t*f[0])*np.exp(-d[0]*t),linewidth=.5)
plt.show() # figure_2