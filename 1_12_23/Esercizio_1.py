import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sympy 
from scipy import integrate
import scipy.constants
import matplotlib.animation as animation




#-------------(V_in=+-1)-------------
##########################################################################################################

# # Definizione dell'equazione differenziale
# def model(V_out, t, RC):
#     V_in = 1.0 if int(t) % 2 == 0 else -1.0
     
#     return (V_in - V_out) / (RC)


# def V_ini(t):
#     if int(t) % 2 == 0:  # Se t è pari
#         return 1.0
#     else:
#         return -1.0

# # Condizioni iniziali e parametri
# RC1 = 1  
# RC2 = 0.1
# RC3 = 0.01

# V_out_initial = 0.0  # Valore iniziale di V_out
# t = np.linspace(0, 10, 1000)  # Intervallo di tempo

# V_in=np.empty(len(t))

# for i in range(0,len(t)):
#     V_in[i]=V_ini(t[i])




# # Risoluzione dell'equazione differenziale
# V_out_1 = integrate.odeint(model, V_out_initial, t, args=( RC1,  ))
# V_out_2 = integrate.odeint(model, V_out_initial, t, args=( RC2,  ))
# V_out_3 = integrate.odeint(model, V_out_initial, t, args=( RC3,  ))

# # Plot del risultato
# fig,((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2, figsize=(9,4))
# ax1.plot(V_in, V_out_1, 'b', label='RC=1')
# ax2.plot(V_in, V_out_2, 'r', label='RC=0.1')
# ax3.plot(V_in, V_out_3, 'g', label='RC=0.01')
# ax4.set_visible(False)
# plt.show()




# fig,((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2, figsize=(9,4))
# ax1.plot(t, V_out_1, 'b', label='RC=1')
# ax2.plot(t, V_out_2, 'r', label='RC=0.1')
# ax3.plot(t, V_out_3, 'g', label='RC=0.01')
# ax4.set_visible(False)
# plt.show()

# #ax[2].plot(t,V_in, 'r', label='V_in')

# plt.show()

# V_out_1 = V_out_1.flatten().tolist()
# V_out_2 = V_out_2.flatten().tolist()  #trasforma in list
# V_out_3 = V_out_3.flatten().tolist()


# #salva i dati 
# df=pd.DataFrame({
#     "time":t,
#     "V_in":V_in,
#     "V_out_1":V_out_1,
#     "V_out_2":V_out_2,
#     "V_out_3":V_out_3})

# df.to_csv("/home/alessandro/Metodi-Computazionali/1_12_23/pippo.csv", sep=",",index=False)


##########################################################################################################

#-------------(V_in=+-1)-------------
##########################################################################################################
# Definizione dell'equazione differenziale

# Definizione dell'equazione differenziale
def model(V_out, t, RC): 
    if int(t) % 2 == 0:
        V_in=1.0
    else:
        V_in=-1.0
     
    return (V_in - V_out) / (RC)


def V_ini(t):
    if int(t) % 2 == 0:  # Se t è pari
        return 1.0
    else:
        return -1.0

# Condizioni iniziali e parametri
RC1 = 1  
RC2 = 0.1
RC3 = 0.01

h=(10-0)/1000


V_out_initial = 0.0  # Valore iniziale di V_out
t = np.arange(0, 10, h )  # Intervallo di tempo

V_in=np.empty(len(t))

for i in range(0,len(t)):
    V_in[i]=V_ini(t[i])







# Risoluzione dell'equazione differenziale
V_out_1 = integrate.odeint(model, V_out_initial, t, args=( RC1,  ))
V_out_2 = integrate.odeint(model, V_out_initial, t, args=( RC2,  ))
V_out_3 = integrate.odeint(model, V_out_initial, t, args=( RC3,  ))





voutsol={}
tsol={}

x=V_out_initial
xx=np.empty((0,0))
for tt,v in zip(t,V_in):
    xx=np.append(xx,x)
    k1=h*model(x,tt,RC3)
    k2=h*model(x+0.5*k1,tt+0.5*h,RC3)
    k3=h*model(x+0.5*k2,tt+0.5*h,RC3)
    k4=h*model(x+0.5*k3,tt+0.5*h,RC3)
    x+=(k1+k1*2+k3*2+k4)/6

voutsol.update({RC3:xx})
tsol.update({RC3:t})






# Plot del risultato
fig,((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2, figsize=(9,4))
ax1.plot(V_in, V_out_1, 'b.', label='RC=1')
ax1.set_ylabel("Tensione V_out(V)")
ax1.set_xlabel("Tensione V_in(V)")


ax2.plot(V_in, V_out_2, 'r.', label='RC=0.1')
ax2.set_ylabel("Tensione V_out(V)")
ax2.set_xlabel("Tensione V_in(V)")

ax3.plot(V_in, V_out_3, 'g.', label='RC=0.01')
ax3.set_ylabel("Tensione V_out(V)")
ax3.set_xlabel("Tensione V_in(V)")

plt.suptitle("Rapporto V_in/V_out")
ax1.set_title('RC=1')
ax2.set_title('RC=0.1')
ax3.set_title('RC=0.01')

ax4.set_visible(False)
plt.show()




fig,((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2, figsize=(9,4))
ax1.plot(t, V_out_1, 'b', label='RC=1')
ax1.plot(t, V_in, 'yellow', label='RC=1',alpha=0.5)
ax1.set_ylabel("Tensione(V)")
ax1.set_xlabel("Tempo(s)")

ax2.plot(t, V_out_2, 'r', label='RC=0.1')
ax2.plot(t, V_in, 'yellow', label='RC=1',alpha=0.5)
ax2.set_ylabel("Tensione(V)")
ax2.set_xlabel("Tempo(s)")



ax3.plot(t, voutsol[RC3], 'g', label='V_out_Rounge')
ax3.plot(t, V_out_3, 'lavender', label='V_out_ode')
ax3.plot(t, V_in, 'yellow', label='V_in',alpha=0.3)
ax3.set_ylabel("Tensione(V)")
ax3.set_xlabel("Tempo(s)")
ax3.legend(loc="best")

ax4.set_visible(False)
ax1.set_title('RC=1')
ax2.set_title('RC=0.1')
ax3.set_title('RC=0.01')
plt.suptitle("V_out in funzione del tempo")
plt.show()

#ax[2].plot(t,V_in, 'r', label='V_in')

plt.show()

V_out_1 = V_out_1.flatten().tolist()
V_out_2 = V_out_2.flatten().tolist()  #trasforma in list
V_out_3 = voutsol[RC3].flatten().tolist()


#salva i dati 
df=pd.DataFrame({
    "time":t,
    "V_in":V_in,
    "V_out_1":V_out_1,
    "V_out_2":V_out_2,
    "V_out_3":V_out_3})

df.to_csv("/home/alessandro/Metodi-Computazionali/1_12_23/pippo.csv", sep=",",index=False)

##########################################################################################################