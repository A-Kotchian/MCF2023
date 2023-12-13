import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sympy 
from scipy import constants,integrate,fftpack,optimize
from scipy.fft import fft, fftfreq, rfft, rfftfreq, ifft
import scipy.constants
import matplotlib.animation as animation
import math
from tqdm import tqdm



"""
-diffusione ha un passo costante s 
-ad ogni passo lo spostamento ha la stessa probabilita (phi tra 0,2pi)
    delta_x=s*cos(phi)
    delta_y=s*sin(phi)
-modulo deve mettere a disposizione una funzione che data s e N il numero di passi , 
    restituisca 2 array con spostamento lungo X e Y perogni N.
"""


def random_walk(s, N):
    deltax = np.array([0])
    tmpx = 0
    phi=np.random.uniform(0,2*np.pi,N)
    for i in range(0,N):
        tmpx = tmpx+s*np.cos(phi[i])
        deltax = np.append(deltax, tmpx)
    

    deltay = np.array([0])
    tmpy = 0
    for i in range(0,N):
        tmpy = tmpy+s*np.sin(phi[i])
        deltay = np.append(deltay, tmpy)
    return deltax,deltay


def spost(x,y):
    
    spostx=np.array([0])
    sposty=np.array([0])
    for i in range(1,len(x)):
        spostx=np.append(spostx,(x[i]-x[0])**2)
        sposty=np.append(sposty,(y[i]-y[0])**2)
    return spostx,sposty


def uniform_phi(N):
    s=np.random.uniform(0,1,N)
    inv_c=2*np.arccos(1-2*s)
    return inv_c

def random_walk_phi(s, N):
    deltax = np.array([0])
    tmpx = 0
    phi=uniform_phi(N)
    for i in range(0,N):
        tmpx = tmpx+s*np.cos(phi[i])
        deltax = np.append(deltax, tmpx)
    

    deltay = np.array([0])
    tmpy = 0
    for i in range(0,N):
        tmpy = tmpy+s*np.sin(phi[i])
        deltay = np.append(deltay, tmpy)
    return deltax,deltay

def uniform_phi_cost(N,c):
    s=np.random.uniform(0,1,N)
    inv_c=2*np.arccos(1-2*s)+c
    return inv_c


def random_walk_phi_cost(s, N,molt):
    deltax = np.array([0])
    tmpx = 0
    c=np.random.uniform(0,300,N)
    phi=uniform_phi(N)
    for i in c:
        if i<=199:
            for i in range(0,N):
                tmpx = tmpx+s*np.cos(phi[i])+molt*c
                deltax = np.append(deltax, tmpx)
        else:
            for i in range(0,N):
                tmpx = tmpx+s*np.cos(phi[i])
                deltax = np.append(deltax, tmpx)

    deltay = np.array([0])
    tmpy = 0
    for i in range(0,N):
        tmpy = tmpy+s*np.sin(phi[i])
        deltay = np.append(deltay, tmpy)
    return deltax,deltay

