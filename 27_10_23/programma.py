import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sympy 

#se devi far prendere il file da un altra parte

"""
import sys

sys.path.append("nome della directory dove sta il file")
#ci metti l import 

se vuoi importare solo 1 o piu  funzioni:

from nome import nome_funzioni
"""
import somme 


n=input("Fino a quale numero vuoi calcolare la somma?\n")
exp=input("Quale esponente vuoi usare?\n")
print("\nLa somma dei primi ",n, " numeri è: " ,somme.sum(int(n)),"\n")
print("\nLa somma delle radici dei primi ",n, " numeri è: ",somme.sumrad(int(n)),"\n")
print("\nLa serie dei primi {:} numeri con esponente {:} è: {:} ".format(n,exp,somme.sommatoria(int(n),alpha=int(exp))))

