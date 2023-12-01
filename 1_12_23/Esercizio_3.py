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
def ddt(r, t,w):
    """
    drdt_molla(r, t, g, o) derivate per equazine differenziale del moto oscillante attenuato di una molla 
    r : vettore con variabili r(x,dx/dt)
    t : variabile tempo
    g : costante gamma = C/(2m) [C: costante di attenuazione, m: massa molla]
    o : omega = k/m [k: costante eleastica molla]
    """
    d0dt = r[1]
    dpdt = -((r[0]**3)*(w)**2)
    return (d0dt, dpdt)

w=10000
r0=[1,1]

time_vec = np.linspace(0, 5, 10000)


"""
derivata_theta=integrate.odeint(d_theta, theta_0, w)
derivata_w=integrate.odeint(d_w, w_0, theta, args=( g,l,  ))
"""

derivata=integrate.odeint(ddt, r0,time_vec,args=(w,))



fig,ax = plt.subplots(2,1,figsize=(9,6))
plt.suptitle("Derivata Pendolo")
ax[0].plot(time_vec,  derivata[:,0], "crimson",label=('Pendolo con l=1 e theta=45°'),alpha=0.4)
ax[0].set_xlabel("time(s)")
ax[0].set_ylabel("funzioni (u.a.)")
ax[0].set_title("0")
ax[0].set_xlim(0,1)


ax[1].plot(time_vec,  derivata[:,1],"lime", label=('Pendolo con l=1 e theta=45°'),alpha=0.4)
ax[1].set_title("w")
ax[1].set_xlabel("time(s)")
ax[1].set_ylabel("funzioni (u.a.)")
ax[1].set_xlim(0,1)
plt.show()




w=10000
r01=[3,1]
r02=[2,1000]
r03=[1,1]


derivata1=integrate.odeint(ddt, r01,time_vec,args=(w,))
derivata2=integrate.odeint(ddt, r02,time_vec,args=(w,))
derivata3=integrate.odeint(ddt, r03,time_vec,args=(w,))







"""
derivata_theta=integrate.odeint(d_theta, theta_0, w)
derivata_w=integrate.odeint(d_w, w_0, theta, args=( g,l,  ))
"""


fig,ax = plt.subplots(2,1,figsize=(9,6))
ax[0].plot(time_vec,  derivata1[:,0], label=('r1'),alpha=0.4)
ax[0].set_title("0")
ax[0].set_xlabel("time(s)")
ax[0].set_ylabel("funzioni (u.a.)")
ax[0].plot(time_vec, derivata2[:,0], label=("r2"),alpha=0.4)
ax[0].set_xlim(0,0.6)

ax[1].plot(time_vec,  derivata1[:,1], label=('w1'),alpha=0.4)
ax[1].plot(time_vec, derivata2[:,1], label=("w2"),alpha=0.4)
ax[1].set_title("w")
ax[1].set_xlabel("time(s)")
ax[1].set_ylabel("funzioni (u.a.)")
ax[1].set_xlim(0,0.6)
plt.show()


plt.plot(time_vec,derivata[:,0],alpha=0.4)
plt.plot(time_vec,derivata1[:,0],alpha=0.4)
plt.plot(time_vec,derivata2[:,0],alpha=0.4)
plt.xlim(0,0.6)
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