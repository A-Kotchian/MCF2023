import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sympy 
from scipy import constants,integrate,fftpack,optimize
from scipy.fft import fft, fftfreq, rfft, rfftfreq, ifft
import scipy.constants
import matplotlib.animation as animation
import math




Copernicus=pd.read_csv("/home/alessandro/Metodi-Computazionali/6_12_23/esercitazione/copernicus_PG_selected.csv")


date_old=np.array(Copernicus["date_old"])
date=np.array(Copernicus["date"])
mean_co_ug=np.array(Copernicus["mean_co_ug/m3"])
mean_nh3_ug=np.array(Copernicus["mean_nh3_ug/m3"])
mean_no2_ug=np.array(Copernicus["mean_no2_ug/m3"])
mean_o3_ug=np.array(Copernicus["mean_o3_ug/m3"])
mean_pm10_ug=np.array(Copernicus["mean_pm10_ug/m3"])
mean_pm2p5_ug=np.array(Copernicus["mean_pm2p5_ug/m3"])
mean_so2_ug=np.array(Copernicus["mean_so2_ug/m3"])

plt.plot(date,mean_co_ug ,'yellowgreen', label='CO')
plt.plot(date,mean_nh3_ug ,'indianred', label='NH3')
plt.plot(date,mean_no2_ug ,'green', label='NO2')
plt.plot(date,mean_o3_ug ,'lightblue', label="O3")
plt.plot(date,mean_pm10_ug,"blue", label='PM10')
plt.plot(date,mean_pm2p5_ug ,'tomato', label='PM2P5')
plt.plot(date,mean_so2_ug ,'tomato', label='SO2')
plt.legend(loc="upper left")
plt.show()

fourier_co=rfft(mean_co_ug)
potenza_fft_co = np.abs(fourier_co[:len(fourier_co)//2])**2
freq_fft_time=0.5*fftfreq(len(fourier_co),d=date[1]-date[0])


plt.plot(freq_fft_time[:len(potenza_fft_co)//2],potenza_fft_co[:len(potenza_fft_co)//2])
# plt.xscale("log")
# plt.yscale("log")
plt.show()
fourier_co_mez = fourier_co[:len(fourier_co)//2]

mask=potenza_fft_co>1.0e7
potenza_filtrata_co=fourier_co_mez[mask]

plt.plot(freq_fft_time[:len(potenza_filtrata_co)//2],potenza_filtrata_co[:len(potenza_filtrata_co)//2])
# plt.xscale("log")
# plt.yscale("log")
plt.show()

#periodicita in 1 anno

co_filtrata=ifft(potenza_filtrata_co)
co_ricalc=ifft(fourier_co_mez)
print("Periodo di : ",1/freq_fft_time[3])
plt.plot(date[:len(co_ricalc)],co_ricalc) #date[:len(co_filtrata)]
plt.plot(date,mean_co_ug)
# plt.xscale("log")
# plt.yscale("log")
plt.show()