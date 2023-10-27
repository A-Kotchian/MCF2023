import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sympy 




df = pd.read_csv("18_10_23/get-mcf-data-main/4FGL_J2202.7+4216_weekly_9_11_2023.csv")

print("Il nome delle colonne sono:\n")

col=df.columns

for i in col:
    print("- ",i)



giuliano = df["Julian Date"]
flusso = df["Photon Flux [0.1-100 GeV](photons cm-2 s-1)"]
er_flusso = df["Photon Flux Error(photons cm-2 s-1)"]




f1 = plt.figure(1)

plt.plot(giuliano,flusso, color='orange')
plt.xlabel('Julian Date')
plt.ylabel('Flux [GeV]')
plt.grid(True)
plt.savefig("foto/data1.png",format="png")
plt.savefig("foto/data1.pdf",format="pdf")



f2 = plt.figure(2)

plt.plot(giuliano,flusso, "." ,color='orange')
plt.xlabel('Julian Date')
plt.ylabel('Flux [GeV]')
plt.grid(True)
plt.savefig("foto/data2.png",format="png")
plt.savefig("foto/data2.pdf",format="pdf")
plt.show()


f3 = plt.figure(3)

plt.errorbar(giuliano,flusso,yerr=er_flusso ,color='orange')
plt.xlabel('Julian Date')
plt.ylabel('Flux [GeV]')
plt.grid(True)
plt.savefig("foto/data3.png",format="png")
plt.savefig("foto/data3.pdf",format="pdf")

plt.show()




df




