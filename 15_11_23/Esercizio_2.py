import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.integrate as integrate

def V(x):
    return 0.1*x**6

def V_quad(x):
    return 0.1*x**2

def V_tetr(x):
    return 0.1*x**4

def V_mod(x):
    return 0.1*abs(x)**(3/2)


xx = np.arange(-5,5.05, 0.1)
plt.plot(xx, V(xx), color='slategray')
plt.axvline(color='k', linewidth=0.5)
plt.xlabel('x')
plt.ylabel(r'V(x)')
plt.plot(4.5, 0.1*4.5**6, 'o', markersize=12, color='tomato') #x0
plt.show()


inip=[]
integr=integrate.simpson(xx,dx=0.1)
"""
for i in range(1,len(xx)+1):
    inip.append(integrate.simpson(xx[:i],dx=0.1))

"""
ind_x0=np.where(xx==4.5)

def periodo(b,f):

    m=5   #massa
    pippo=np.arange(0,b,0.1)
    Val=f(pippo)
    p=np.sqrt(8*m)*integrate.simpson((1/(np.sqrt((f(b))-Val))),dx=0.1)
    return p

print("Il periodo da 0 a x0 con ^6 è di : " , periodo(4.5,V),"\n")
print("Il periodo da 0 a x0 con ^2 è di : " , periodo(4.5,V_quad),"\n")
print("Il periodo da 0 a x0 con ^4 è di : " , periodo(4.5,V_tetr),"\n")
print("Il periodo da 0 a x0 con ^3/2 è di : " , periodo(4.5,V_mod),"\n")


#ALLA 6
ciao=np.arange(1,50,0.2)
Per=np.zeros(len(ciao))
for i in range(0,len(ciao)):
    Per[i]=periodo(ciao[i],V)

#ALLA 2
ciao=np.arange(1,50,0.2)
Per_quad=np.zeros(len(ciao))
for i in range(0,len(ciao)):
    Per_quad[i]=periodo(ciao[i],V_quad)

#ALLA 4
ciao=np.arange(1,50,0.2)
Per_tetr=np.zeros(len(ciao))
for i in range(0,len(ciao)):
    Per_tetr[i]=periodo(ciao[i],V_tetr)

#ALLA modulo
ciao=np.arange(1,50,0.2)
Per_mod=np.zeros(len(ciao))
for i in range(0,len(ciao)):
    Per_mod[i]=periodo(ciao[i],V_mod)

plt.plot(ciao, Per, color='slategray')
plt.plot(ciao, Per_quad, color='seagreen')
plt.plot(ciao, Per_tetr, color='indianred')
plt.plot(ciao, Per_mod, color='lightblue')
plt.xlabel('x')
plt.yscale('log')
plt.ylabel('T(s)')
plt.show()


