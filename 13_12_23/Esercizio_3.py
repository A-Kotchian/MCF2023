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
from funzioni import random_walk,spost


def random_walk(su,sf):
    phi=np.random.uniform(0,2*np.pi)
    x=su*np.cos(phi)+sf
    y=su*np.sin(phi)
    return x,y



class Particella():

    def __init__(self,n_coppie,spessore):
        self.spessore=spessore
        self.n_coppie=n_coppie

    def passaggio(self):
        numero_coppie=np.random.poisson(self.n_coppie)
        posizione_coppie=np.random.uniform(-(self.spessore)/2,(self.spessore/2),size=numero_coppie)
        return posizione_coppie,numero_coppie

    def simulazione(self, su, sf, nr, tc, spessore,pos):
        """
        Simulates a process and returns the drift time.

        Args:

        Returns:
            float: Drift time.
        """
        # Check if the initial position is positive
        

        if pos > 0:
            sf = -sf

        pos_y = [pos]
        pos_x = [0]
        passo=0
        while abs(pos_y[-1]) < spessore:
            # Generate a random angle between 0 and 2*pi
            angolo = np.random.uniform(0, 2 * np.pi, 1)

            # Update the position of the pairs
            w=random_walk(su,sf)
            pos_y.append(w[0])
            pos_x.append(w[1])
            # Generate a random absorption factor between 1 and 1/nr
            assorbimento = np.random.binomial(1, 1 / nr,size=None)
            if assorbimento == 1:
                # If absorption factor is 1, break out of the loop
                tempo_deriva = 0
                break
            else:
                passo=passo+1

        tempo_deriva=passo*tc
        return tempo_deriva



su=10**(-6)
sf=5*10**(-5)
nr=10**(4)
tc=10**(-12)
#n_p=5
spessore=0.1
ciao=0
n_media=5
n_p=input("Quante particelle vuoi far passare?\n")
print("\nSIMULANDO\n")
tempo=[]
tem=[]
for i in tqdm(range(0,int(n_p))):
    camera=Particella(n_media,spessore)
    posizione=camera.passaggio()[0]
    print("\nParticella n°",i+1,"\n")
    for j in tqdm(range(0,len(posizione))):
        pos=posizione[j]
        tempo.append(camera.simulazione(su, sf, nr, tc, spessore,pos))
    tem.append(tempo)
    

# mask=tempo!=0
# t=tempo[mask]
t=np.array([0])
for i in range(len(tem)):
    t=np.concatenate((t,tem[i]))

print("\nParticelle cariche :\n ",len(t))
print("Tempo di deriva:\n",t)
print("Tempo minimo di deriva per evento", min(t))
print("Tempo medio di deriva per evento", np.mean(t))


plt.hist(t, bins=3, density=True, alpha=0.6, color='g')
plt.title("tempo per ogni particella")
plt.show

plt.hist(min(t),bins=3, density=True, alpha=0.6, color='y')
plt.title("tempo minimo di deriva")
plt.show()

plt.hist(np.mean(t),bins=3, density=True, alpha=0.6, color='b')
plt.title("tempo medio di deriva")
plt.show()

print("\nL'efficenza del rivelatore è: {:}".format((t/np.mean(t))))