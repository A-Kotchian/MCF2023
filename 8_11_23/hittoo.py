import reco
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sympy
import math
import somme 


def metodone(a):
    file=pd.read_csv(a)
    id=file["det_id"]
    tempi=file["hit_time"]
    modi=file["mod_id"]
    rec=np.empty(len(modi),dtype=reco.Hit)
    for i in range(0,len(modi)):
        rec[i]=reco.Hit(modi[i],id[i],tempi[i])
    return rec

#Raccolta file e dati 

rec_0=metodone("/home/alessandro/Metodi-Computazionali/27_10_23/dati/hit_times_M0.csv")
rec_1=metodone("/home/alessandro/Metodi-Computazionali/27_10_23/dati/hit_times_M1.csv")
rec_2=metodone("/home/alessandro/Metodi-Computazionali/27_10_23/dati/hit_times_M2.csv")
rec_3=metodone("/home/alessandro/Metodi-Computazionali/27_10_23/dati/hit_times_M3.csv")


ordinato=[]
dati_tot=np.concatenate((rec_0,rec_1,rec_2,rec_3))
ordinato=np.sort(dati_tot)

print(ordinato)
print(dati_tot)
print(rec_0)

diff_temp=np.diff(ordinato)

plt.hist(diff_temp, bins=50, range=(0,10))

plt.show()



