import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sympy 
from scipy import integrate
import scipy.constants
import matplotlib.animation as animation
import math


"""
def  d_theta(w):
    return w

def d_w(theta,g,l):
    return -(g/l)*np.sin(theta)

"""
def ddt(r, t, g, l):
    """
    drdt_molla(r, t, g, o) derivate per equazine differenziale del moto oscillante attenuato di una molla 
    r : vettore con variabili r(x,dx/dt)
    t : variabile tempo
    g : costante gamma = C/(2m) [C: costante di attenuazione, m: massa molla]
    o : omega = k/m [k: costante eleastica molla]
    """
    d0dt = r[1]
    dwdt = -(g/l)*np.sin(r[0])
    return (d0dt, dwdt)


l=0.5 #m
theta_0=45 #°
w_0=0 #adimensionale 
g=9.81
yinit=(math.radians(45),0)
theta=np.linspace(0,360,1)
time_vec = np.linspace(0, 10, 100)


"""
derivata_theta=integrate.odeint(d_theta, theta_0, w)
derivata_w=integrate.odeint(d_w, w_0, theta, args=( g,l,  ))
"""

derivata=integrate.odeint(ddt, yinit,time_vec,args=(g,l,))



fig,ax = plt.subplots(2,1,figsize=(9,6))
plt.suptitle("Derivata Pendolo")
ax[0].plot(time_vec,  derivata[:,0], "crimson",label=('Pendolo con l=1 e theta=45°'))
ax[0].set_xlabel("time(s)")
ax[0].set_ylabel("funzioni (u.a.)")
ax[0].set_title("0")


ax[1].plot(time_vec,  derivata[:,1],"lime", label=('Pendolo con l=1 e theta=45°'))
ax[1].set_title("w")
ax[1].set_xlabel("time(s)")
ax[1].set_ylabel("funzioni (u.a.)")

plt.show()


l1=1 #m
l2=0.5 #m
theta_0_1=45 #°
theta_0_2=30 #°
w_0=0 #adimensionale 
g=9.81
yinit1=(math.radians(45),0)  #theta_0
yinit2=(math.radians(30),0) #theta_0
time_vec = np.linspace(0, 10, 100)


"""
derivata_theta=integrate.odeint(d_theta, theta_0, w)
derivata_w=integrate.odeint(d_w, w_0, theta, args=( g,l,  ))
"""

derivata1=integrate.odeint(ddt, yinit1,time_vec,args=(g,l1,))
derivata2=integrate.odeint(ddt, yinit2,time_vec,args=(g,l2,))



fig,ax = plt.subplots(2,1,figsize=(9,6))
ax[0].plot(time_vec,  derivata1[:,0], label=('Pendolo con l=1 e theta=45°'))
ax[0].set_title("0")
ax[0].set_xlabel("time(s)")
ax[0].set_ylabel("funzioni (u.a.)")
ax[0].plot(time_vec, derivata2[:,0], label=("Pendolo con l=0.5 e theta=30°"))


ax[1].plot(time_vec,  derivata1[:,1], label=('Pendolo con l=1 e theta=45°'))
ax[1].plot(time_vec, derivata2[:,1], label=("Pendolo con l=0.5 e theta=30°"))
ax[1].set_title("w")
ax[1].set_xlabel("time(s)")
ax[1].set_ylabel("funzioni (u.a.)")
plt.show()


plt.plot(time_vec,derivata[:,0])
plt.plot(time_vec,derivata1[:,0])
plt.plot(time_vec,derivata2[:,0])
plt.show()

#confronto:
"""
diff_d0dt = derivata1[:, 0] - derivata2[:, 0]
diff_dwdt = derivata1[:, 1] - derivata2[:, 1]

fig,(ax1,ax2)= plt.subplots(2,1)
ax1.plot(time_vec, diff_d0dt,"r", '-')
ax1.set_title("d0dt")
ax1.set_xlabel("time(s)")
ax1.set_ylabel("funzioni (u.a.)")

ax2.plot(time_vec,  diff_dwdt,"b","--")
ax2.set_title("dwdt")
ax2.set_xlabel("time(s)")
ax2.set_ylabel("funzioni (u.a.)")
plt.show()
"""