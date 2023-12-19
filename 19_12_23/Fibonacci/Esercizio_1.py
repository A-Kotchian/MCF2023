import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.integrate as integrate
import ctypes
import sys
import Fibonacci.serie as serie






print("Benvenuto nel calcolatore della serie di Fibonacci!\nInserisci fino a che numero vuoi calcolare la serie")
b=input("\nNumero: ")
if int(b)==0:
    print("\nMi dispiace ma la serie non funzione :(\n")

else:
    print("Il valore della serie di Fibonacci per il numero ",b," è ",serie.fibonacci(int(b)))