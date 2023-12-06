import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sympy 
from scipy import constants,integrate,fftpack,optimize
from scipy.fft import fft, fftfreq, rfft, rfftfreq, ifft
import scipy.constants
import matplotlib.animation as animation
import math




BiLac=pd.read_csv("/home/alessandro/Metodi-Computazionali/6_12_23/esercitazione/4FGL_J2202.7+4216_weekly_9_15_2023_mcf.csv")
S5=pd.read_csv("/home/alessandro/Metodi-Computazionali/6_12_23/esercitazione/4FGL_J0721.9+7120_weekly_9_15_2023_mcf.csv")
PKS=pd.read_csv("/home/alessandro/Metodi-Computazionali/6_12_23/esercitazione/4FGL_J0428.6-3756_weekly_9_15_2023_mcf.csv")
C3279=pd.read_csv("/home/alessandro/Metodi-Computazionali/6_12_23/esercitazione/4FGL_J1256.1-0547_weekly_9_15_2023_mcf.csv")
C3454=pd.read_csv("/home/alessandro/Metodi-Computazionali/6_12_23/esercitazione/4FGL_J2253.9+1609_weekly_9_15_2023_mcf.csv")
CTA=pd.read_csv("/home/alessandro/Metodi-Computazionali/6_12_23/esercitazione/4FGL_J2232.6+1143_weekly_9_15_2023_mcf.csv")


date_BiLac=np.array(BiLac["Date(UTC)"])
julian_BiLac=np.array(BiLac["Julian Date"])
TS_BiLac=np.array(BiLac["TS"])
Photon_flux_BiLac=np.array(BiLac["Photon Flux [0.1-100 GeV](photons cm-2 s-1)"])
Photon_flux_err_BiLac=np.array(BiLac["Photon Flux Error(photons cm-2 s-1)"])

date_S5=np.array(S5["Date(UTC)"])
julian_S5=np.array(S5["Julian Date"])
TS_S5=np.array(S5["TS"])
Photon_flux_S5=np.array(S5["Photon Flux [0.1-100 GeV](photons cm-2 s-1)"])
Photon_flux_err_S5=np.array(S5["Photon Flux Error(photons cm-2 s-1)"])

date_PKS=np.array(PKS["Date(UTC)"])
julian_PKS=np.array(PKS["Julian Date"])
TS_PKS=np.array(PKS["TS"])
Photon_flux_PKS=np.array(PKS["Photon Flux [0.1-100 GeV](photons cm-2 s-1)"])
Photon_flux_err_PKS=np.array(PKS["Photon Flux Error(photons cm-2 s-1)"])

date_C3279=np.array(C3279["Date(UTC)"])
julian_C3279=np.array(C3279["Julian Date"])
TS_C3279=np.array(C3279["TS"])
Photon_flux_C3279=np.array(C3279["Photon Flux [0.1-100 GeV](photons cm-2 s-1)"])
Photon_flux_err_C3279=np.array(C3279["Photon Flux Error(photons cm-2 s-1)"])

date_C3454=np.array(C3454["Date(UTC)"])
julian_C3454=np.array(C3454["Julian Date"])
TS_C3454=np.array(C3454["TS"])
Photon_flux_C3454=np.array(C3454["Photon Flux [0.1-100 GeV](photons cm-2 s-1)"])
Photon_flux_err_C3454=np.array(C3454["Photon Flux Error(photons cm-2 s-1)"])

date_CTA=np.array(CTA["Date(UTC)"])
julian_CTA=np.array(CTA["Julian Date"])
TS_CTA=np.array(CTA["TS"])
Photon_flux_CTA=np.array(CTA["Photon Flux [0.1-100 GeV](photons cm-2 s-1)"])
Photon_flux_err_CTA=np.array(CTA["Photon Flux Error(photons cm-2 s-1)"])




plt.plot(julian_BiLac,Photon_flux_BiLac ,'yellowgreen', label='BiLac')
plt.plot(julian_S5,Photon_flux_S5 ,'indianred', label='S5')
plt.plot(julian_PKS,Photon_flux_PKS ,'green', label='PKS')
plt.plot(julian_C3279,Photon_flux_C3279 ,'lightblue', label='C3279')
plt.plot(julian_C3454,Photon_flux_C3454 ,"blue", label='C3454')
plt.plot(julian_CTA,Photon_flux_CTA ,'tomato', label='CTA')
plt.legend(loc="upper left")
plt.show()

# Plot del risultato
fig,((ax1,ax2),(ax3,ax4),(ax5,ax6)) = plt.subplots(3,2, figsize=(9,9))
ax1.errorbar(julian_BiLac,Photon_flux_BiLac, yerr=Photon_flux_err_BiLac , fmt='-',color="yellowgreen", label='BiLac')
ax1.set_ylabel("Flusso")
ax1.set_xlabel("Giorno Giuliano")

ax3.errorbar(julian_S5,Photon_flux_S5, yerr=Photon_flux_err_S5 , fmt='-',color="yellowgreen", label='S5')
ax3.set_ylabel("Flusso")
ax3.set_xlabel("Giorno Giuliano")

ax5.errorbar(julian_PKS,Photon_flux_PKS, yerr=Photon_flux_err_PKS , fmt='-', color="yellowgreen",label='PKS')
ax5.set_ylabel("Flusso")
ax5.set_xlabel("Giorno Giuliano")

ax4.errorbar(julian_C3279,Photon_flux_C3279, yerr=Photon_flux_err_C3279 , fmt='-',color="rebeccapurple" ,label='C3279')
ax4.set_ylabel("Flusso")
ax4.set_xlabel("Giorno Giuliano")

ax2.errorbar(julian_C3454,Photon_flux_C3454, yerr=Photon_flux_err_C3454 , fmt='-', color="rebeccapurple",label='C3454')
ax2.set_ylabel("Flusso")
ax2.set_xlabel("Giorno Giuliano")

ax6.errorbar(julian_CTA,Photon_flux_CTA, yerr=Photon_flux_err_CTA , fmt='-',color="rebeccapurple", label='CTA')
ax6.set_ylabel("Flusso")
ax6.set_xlabel("Giorno Giuliano")

plt.suptitle("Giorno Giuliano-Flusso:")
ax1.legend(loc="best")
ax2.legend(loc="best")
ax3.legend(loc="best")
ax4.legend(loc="best")
ax5.legend(loc="best")
ax6.legend(loc="best")

ax1.set_title("BLL")
ax2.set_title("FSRQ")

plt.show()




fourier_BiLac=rfft(Photon_flux_BiLac)
fourier_S5=rfft(Photon_flux_S5)
fourier_PKS=rfft(Photon_flux_PKS)
fourier_C3279=rfft(Photon_flux_C3279)
fourier_C3454=rfft(Photon_flux_C3454)
fourier_CTA=rfft(Photon_flux_CTA)


potenza_fft_BiLac = np.abs(fourier_BiLac[:len(fourier_BiLac)//2])**2
potenza_fft_S5 = np.abs(fourier_S5[:len(fourier_S5)//2])**2
potenza_fft_PKS = np.abs(fourier_PKS[:len(fourier_PKS)//2])**2
potenza_fft_C3279 = np.abs(fourier_C3279[:len(fourier_C3279)//2])**2
potenza_fft_C3454 = np.abs(fourier_C3454[:len(fourier_C3454)//2])**2
potenza_fft_CTA = np.abs(fourier_CTA[:len(fourier_CTA)//2])**2


freq_fft_BiLac=0.5*fftfreq(len(fourier_BiLac),d=julian_BiLac[1]-julian_BiLac[0])
freq_fft_S5=0.5*fftfreq(len(fourier_S5),d=julian_S5[1]-julian_S5[0])
freq_fft_PKS=0.5*fftfreq(len(fourier_PKS),d=julian_PKS[1]-julian_PKS[0])
freq_fft_C3279=0.5*fftfreq(len(fourier_C3279),d=julian_C3279[1]-julian_C3279[0])
freq_fft_C3454=0.5*fftfreq(len(fourier_C3454),d=julian_C3454[1]-julian_C3454[0])
freq_fft_CTA=0.5*fftfreq(len(fourier_CTA),d=julian_CTA[1]-julian_CTA[0])




plt.plot(freq_fft_BiLac[:len(potenza_fft_BiLac)//2],potenza_fft_BiLac[:len(potenza_fft_BiLac)//2],"yellowgreen", label='BiLac')
plt.plot(freq_fft_S5[:len(potenza_fft_S5)//2],potenza_fft_S5[:len(potenza_fft_S5)//2], "yellowgreen", label='S5')
plt.plot(freq_fft_PKS[:len(potenza_fft_PKS)//2],potenza_fft_PKS[:len(potenza_fft_PKS)//2], "yellowgreen",label='PKS')
plt.plot(freq_fft_C3279[:len(potenza_fft_C3279)//2],potenza_fft_C3279[:len(potenza_fft_C3279)//2],"rebeccapurple" ,label='C3279')
plt.plot(freq_fft_C3454[:len(potenza_fft_C3454)//2], potenza_fft_C3454[:len(potenza_fft_C3454)//2], "rebeccapurple",label='C3454')
plt.plot(freq_fft_CTA[:len(potenza_fft_CTA)//2],potenza_fft_CTA[:len(potenza_fft_CTA)//2], "rebeccapurple", label='CTA')
plt.ylabel("Potenza")
plt.legend(loc="upper right")
plt.xlabel("frequenza")
plt.xscale("log")
plt.yscale("log")
plt.show()

fig,((ax1,ax2),(ax3,ax4),(ax5,ax6)) = plt.subplots(3,2, figsize=(9,9))
ax1.plot(freq_fft_BiLac[:len(potenza_fft_BiLac)//2],potenza_fft_BiLac[:len(potenza_fft_BiLac)//2],"yellowgreen", label='BiLac')
ax1.set_ylabel("Potenza")
ax1.set_xlabel("frequenza")

ax3.plot(freq_fft_S5[:len(potenza_fft_S5)//2],potenza_fft_S5[:len(potenza_fft_S5)//2], "yellowgreen", label='S5')
ax3.set_ylabel("Potenza")
ax3.set_xlabel("frequenza")

ax5.plot(freq_fft_PKS[:len(potenza_fft_PKS)//2],potenza_fft_PKS[:len(potenza_fft_PKS)//2], "yellowgreen",label='PKS')
ax5.set_ylabel("Potenza")
ax5.set_xlabel("frequenza")

ax4.plot(freq_fft_C3279[:len(potenza_fft_C3279)//2],potenza_fft_C3279[:len(potenza_fft_C3279)//2],"rebeccapurple" ,label='C3279')
ax4.set_ylabel("Potenza")
ax4.set_xlabel("frequenza")

ax2.plot(freq_fft_C3454[:len(potenza_fft_C3454)//2], potenza_fft_C3454[:len(potenza_fft_C3454)//2], "rebeccapurple",label='C3454')
ax2.set_ylabel("Potenza")
ax2.set_xlabel("frequenza")

ax6.plot(freq_fft_CTA[:len(potenza_fft_CTA)//2],potenza_fft_CTA[:len(potenza_fft_CTA)//2], "rebeccapurple", label='CTA')
ax6.set_ylabel("Potenza")
ax6.set_xlabel("frequenza")

plt.suptitle("Potenza-frequenza:")
ax1.legend(loc="best")
ax2.legend(loc="best")
ax3.legend(loc="best")
ax4.legend(loc="best")
ax5.legend(loc="best")
ax6.legend(loc="best")

ax1.set_title("BLL")
ax2.set_title("FSRQ")

plt.show()


fig,((ax1,ax2),(ax3,ax4),(ax5,ax6)) = plt.subplots(3,2, figsize=(9,9))
ax1.plot(freq_fft_BiLac[:len(potenza_fft_BiLac)//2],potenza_fft_BiLac[:len(potenza_fft_BiLac)//2],"yellowgreen", label='BiLac')
ax1.set_ylabel("Potenza")
ax1.set_xlabel("frequenza")

ax3.plot(freq_fft_S5[:len(potenza_fft_S5)//2],potenza_fft_S5[:len(potenza_fft_S5)//2]/potenza_fft_BiLac[0], "yellowgreen", label='S5')
ax3.set_ylabel("Potenza")
ax3.set_xlabel("frequenza")

ax5.plot(freq_fft_PKS[:len(potenza_fft_PKS)//2],potenza_fft_PKS[:len(potenza_fft_PKS)//2]/potenza_fft_S5[0], "yellowgreen",label='PKS')
ax5.set_ylabel("Potenza")
ax5.set_xlabel("frequenza")

ax4.plot(freq_fft_C3279[:len(potenza_fft_C3279)//2],potenza_fft_C3279[:len(potenza_fft_C3279)//2]/potenza_fft_C3279[0],"rebeccapurple" ,label='C3279')
ax4.set_ylabel("Potenza")
ax4.set_xlabel("frequenza")

ax2.plot(freq_fft_C3454[:len(potenza_fft_C3454)//2], potenza_fft_C3454[:len(potenza_fft_C3454)//2]/potenza_fft_C3454[0], "rebeccapurple",label='C3454')
ax2.set_ylabel("Potenza")
ax2.set_xlabel("frequenza")

ax6.plot(freq_fft_CTA[:len(potenza_fft_CTA)//2],potenza_fft_CTA[:len(potenza_fft_CTA)//2]/potenza_fft_CTA[0], "rebeccapurple", label='CTA')
ax6.set_ylabel("Potenza")
ax6.set_xlabel("frequenza")

plt.suptitle("Potenza-frequenza normalizzati:")
ax1.legend(loc="best")
ax2.legend(loc="best")
ax3.legend(loc="best")
ax4.legend(loc="best")
ax5.legend(loc="best")
ax6.legend(loc="best")

ax1.set_title("BLL")
ax2.set_title("FSRQ")

ax1.set_xscale("log")
ax2.set_xscale("log")
ax3.set_xscale("log")
ax4.set_xscale("log")
ax5.set_xscale("log")
ax6.set_xscale("log")


ax1.set_yscale("log")
ax2.set_yscale("log")
ax3.set_yscale("log")
ax4.set_yscale("log")
ax5.set_yscale("log")
ax6.set_yscale("log")

plt.show()



plt.plot(freq_fft_BiLac[:len(potenza_fft_BiLac)//2],potenza_fft_BiLac[:len(potenza_fft_BiLac)//2]/potenza_fft_BiLac[0],"yellowgreen", label='BiLac')
plt.plot(freq_fft_S5[:len(potenza_fft_S5)//2],potenza_fft_S5[:len(potenza_fft_S5)//2]/potenza_fft_S5[0], "yellowgreen", label='S5')
plt.plot(freq_fft_PKS[:len(potenza_fft_PKS)//2],potenza_fft_PKS[:len(potenza_fft_PKS)//2]/potenza_fft_PKS[0], "yellowgreen",label='PKS')
plt.plot(freq_fft_C3279[:len(potenza_fft_C3279)//2],potenza_fft_C3279[:len(potenza_fft_C3279)//2]/potenza_fft_C3279[0],"rebeccapurple" ,label='C3279')
plt.plot(freq_fft_C3454[:len(potenza_fft_C3454)//2], potenza_fft_C3454[:len(potenza_fft_C3454)//2]/potenza_fft_C3454[0], "rebeccapurple",label='C3454')
plt.plot(freq_fft_CTA[:len(potenza_fft_CTA)//2],potenza_fft_CTA[:len(potenza_fft_CTA)//2]/potenza_fft_CTA[0], "rebeccapurple", label='CTA')
plt.ylabel("Potenza")
plt.legend(loc="upper right")
plt.xlabel("frequenza")
plt.xscale("log")
plt.yscale("log")
plt.show()

# params1,params_covariance1= optimize.curve_fit(funzione,xdata=freq1[mask1],ydata=data1_fft[mask1],p0=[0,100])
# err_data1=np.sqrt(np.diag(params_covariance1))
# y_fit_data1 = funzione(freq1,params1[0],params1[1])

