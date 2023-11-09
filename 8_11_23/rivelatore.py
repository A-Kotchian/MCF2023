import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sympy
import math
import somme 




#Raccolta file e dati 
file_0 = pd.read_csv("/home/alessandro/Metodi-Computazionali/27_10_23/dati/hit_times_M0.csv")
id_0 = file_0["det_id"]
tempi_0 = file_0["hit_time"]     
file_0



file_1 = pd.read_csv("/home/alessandro/Metodi-Computazionali/27_10_23/dati/hit_times_M1.csv")
id_1 = file_1["det_id"]
tempi_1 = file_1["hit_time"] 
file_1



file_2 = pd.read_csv("/home/alessandro/Metodi-Computazionali/27_10_23/dati/hit_times_M2.csv")
id_2 = file_2["det_id"]
tempi_2 = file_2["hit_time"]   
file_2



file_3 = pd.read_csv("/home/alessandro/Metodi-Computazionali/27_10_23/dati/hit_times_M3.csv")
id_3 = file_3["det_id"]
tempi_3 = file_3["hit_time"]               

file_3



#istogramma dati

fig = plt.figure()      
gs = fig.add_gridspec(2, 2, hspace=0, wspace=0) 
(ax1,ax2),(ax3,ax4)= gs.subplots(sharex="col",sharey="row")

ax1.hist(tempi_0, bins=100,range=(0,1000000000)  ,color='blue', alpha=0.2 )
ax2.hist(tempi_1, bins=100,range=(0,1000000000) ,color='g', alpha=0.2 )
ax3.hist(tempi_2, bins=100,range=(0,1000000000)  ,color='k', alpha=0.2)
ax4.hist(tempi_3, bins=100,range=(0,1000000000)  ,color='r', alpha=0.2 )

ax3.sharey(ax4)
ax3.sharex(ax1)
ax2.sharex(ax4)
ax2.sharey(ax1)


ax1.set_ylabel("Bins")
ax3.set_xlabel("Tempi (s)")
ax3.set_ylabel("Bins") 
ax4.set_xlabel("Tempi (s)")
fig.suptitle("Tempi di hit e istogramma dati", fontsize=16)

plt.show()

lung_0=len(tempi_0)
lung_1=len(tempi_1)
lung_2=len(tempi_2)
lung_3=len(tempi_3)

print(lung_0,lung_1,lung_2,lung_3)

#differenza hit e istrogramma dati

diff_t_0=np.log10(np.diff(tempi_0))
diff_t_1=np.log10(np.diff(tempi_1))
diff_t_2=np.log10(np.diff(tempi_2))
diff_t_3=np.log10(np.diff(tempi_3))


print(diff_t_0[1])

#grafico distanza tempi di hit e istogramma dati
fig = plt.figure()      
gs = fig.add_gridspec(2, 2, hspace=0, wspace=0) 
(ax1,ax2),(ax3,ax4)= gs.subplots(sharex="col",sharey="row")

ax1.hist(diff_t_0, bins=50,range=(0,6)  ,color='blue', alpha=0.2 )
ax2.hist(diff_t_1, bins=50,range=(0,6) ,color='g', alpha=0.2 )
ax3.hist(diff_t_2, bins=50,range=(0,6)  ,color='k', alpha=0.2)
ax4.hist(diff_t_3, bins=50,range=(0,6)  ,color='r', alpha=0.2 )

ax3.sharey(ax4)
ax3.sharex(ax1)
ax2.sharex(ax4)
ax2.sharey(ax1)


ax1.set_ylabel("Bins")
ax3.set_xlabel("log_10-Delta Tempi (s)")
ax3.set_ylabel("Bins") 
ax4.set_xlabel("log_10-Delta Tempi (s)")
fig.suptitle("Differenza delta Tempi di hit in log10 e istogramma dati ", fontsize=16)
plt.show()

# Coordinate centro Moduli [m]
xmod = [-5,  5, -5,  5]
ymod = [ 5,  5, -5, -5]
        
# Coordinate dei Sensori rispetto al centro del Modulo [m]
xdet = [-2.5, 2.5, 0, -2.5,  2.5]
ydet = [ 2.5, 2.5, 0, -2.5, -2.5]


