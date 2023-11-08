import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sympy 

def sum(n):
    somma=0
    for i in range(1,n+1):
        somma=somma+i
    return somma

def sumrad(n):
    somma=0
    for i in range(1,n+1):
        somma=somma+(np.sqrt(i))
    return somma


def sum_prod(n):
    somma=0
    prodotto=0
    for i in range(1,n+1):
        somma=somma+i
        prodotto=prodotto*i
    return somma,prodotto

def sommatoria(n,**kwargs):
    somma=0
    exp=1
    for key, value in kwargs.items():

        if key == "alpha":
            exp=value
        else:
            exp=1
    for i in range(0,n+1):
        somma=somma+i**exp
    return somma
        