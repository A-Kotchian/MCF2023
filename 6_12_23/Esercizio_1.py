import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sympy 
from scipy import constants,integrate,fftpack,optimize
from scipy.fft import fft, fftfreq, rfft, rfftfreq, ifft
import scipy.constants
import matplotlib.animation as animation
import math


def funzione(f,b,A):
    return A/((f)**b)


data1=pd.read_csv("/home/alessandro/Metodi-Computazionali/6_12_23/esercitazione/data_sample1.csv")
data2=pd.read_csv("/home/alessandro/Metodi-Computazionali/6_12_23/esercitazione/data_sample2.csv")
data3=pd.read_csv("/home/alessandro/Metodi-Computazionali/6_12_23/esercitazione/data_sample3.csv")


time_data1=np.array(data1["time"])
meas_data1=np.array(data1["meas"])


time_data2=np.array(data2["time"])
meas_data2=np.array(data2["meas"])


time_data3=np.array(data3["time"])
meas_data3=np.array(data3["meas"])


# Plot del risultato
fig,((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2, figsize=(9,4))
ax1.plot(time_data1, meas_data1 , 'b-', label='data1')
ax1.set_ylabel("meas(u.a.)")
ax1.set_xlabel("time(s)")

ax2.plot(time_data2, meas_data2 , 'r-', label='data2')
ax2.set_ylabel("meas(u.a.)")
ax2.set_xlabel("time(s)")

ax3.plot(time_data3, meas_data3, 'g-', label='data3')
ax3.set_ylabel("meas(u.a.)")
ax3.set_xlabel("time(s)")

plt.suptitle("meas-time")
ax1.legend(loc="best")
ax2.legend(loc="best")
ax3.legend(loc="best")

ax4.set_visible(False)
plt.show()


# data1_fft=rfft(meas_data1)
# data2_fft=rfft(meas_data2)
# data3_fft=rfft(meas_data3)

data1_fft = np.abs(rfft(meas_data1)[:len(rfft(meas_data1))//2])**2
data2_fft = np.abs(rfft(meas_data2)[:len(rfft(meas_data2))//2])**2
data3_fft = np.abs(rfft(meas_data3)[:len(rfft(meas_data3))//2])**2

dt=data1_fft[1]-data1_fft[0]
freq1=0.5*fftfreq(len(data1_fft),dt)
freq2=0.5*fftfreq(len(data2_fft),dt)
freq3=0.5*fftfreq(len(data3_fft),dt)

mask1=np.logical_and(freq1>1.2e-06,freq1!=0)
mask2=np.logical_and(freq2>0,freq2!=0)
mask3=np.logical_and(freq3>1.2e-06,freq3!=0)

fig,((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2, figsize=(9,4))
ax1.plot(freq1[mask1], data1_fft[mask1] , 'b-', label='data1')
ax1.set_ylabel("meas(u.a.)")
ax1.set_xlabel("time(s)")

ax2.plot(freq2[mask2], data2_fft[mask2] , 'r-', label='data2')
ax2.set_ylabel("meas(u.a.)")
ax2.set_xlabel("time(s)")

ax3.plot(freq3[mask3], data3_fft[mask3], 'g-', label='data3')
ax3.set_ylabel("meas(u.a.)")
ax3.set_xlabel("time(s)")

plt.suptitle("fft of meas-time")
ax1.legend(loc="best")
ax2.legend(loc="best")
ax3.legend(loc="best")

ax4.set_visible(False)
plt.show()


params1,params_covariance1= optimize.curve_fit(funzione,xdata=freq1[mask1],ydata=data1_fft[mask1],p0=[0,100])
err_data1=np.sqrt(np.diag(params_covariance1))
y_fit_data1 = funzione(freq1,params1[0],params1[1])


params2,params_covariance2= optimize.curve_fit(funzione,xdata=freq2[mask2],ydata=data2_fft[mask2],p0=[1,100])
err_data2=np.sqrt(np.diag(params_covariance2))
y_fit_data2 = funzione(freq2,params2[0],params2[1])


params3,params_covariance3= optimize.curve_fit(funzione,xdata=freq3[mask3],ydata=data3_fft[mask3],p0=[2,100])
err_data3=np.sqrt(np.diag(params_covariance3))
y_fit_data3 = funzione(freq3,params3[0],params3[1])



fig,((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2, figsize=(9,4))
ax1.plot(freq1[mask1], data1_fft[mask1] , 'b-', label='data1')
ax1.plot(freq1[mask1], y_fit_data1[mask1] ,"y-", label='fit1')
ax1.set_ylabel("meas(u.a.)")
ax1.set_xlabel("time(s)")
ax1.set_xscale("log")
ax1.set_yscale("log")



mask=freq2>0
ax2.plot(freq2[mask2], data2_fft[mask2] , 'r-', label='data2')
ax2.plot(freq2[mask2], y_fit_data2[mask2] ,"y-", label='fit2')
ax2.set_ylabel("meas(u.a.)")
ax2.set_xlabel("time(s)")
ax2.set_xscale("log")
ax2.set_yscale("log")


mask=freq3>0
ax3.plot(freq3[mask3], data3_fft[mask3], 'g-', label='data3')
ax3.plot(freq3[mask3], y_fit_data3[mask3] ,"y-" , label='fit3')
ax3.set_ylabel("meas(u.a.)")
ax3.set_xlabel("time(s)")
ax3.set_xscale("log")
ax3.set_yscale("log")

plt.suptitle("fft of meas-time and fits")
ax1.legend(loc="best")
ax2.legend(loc="best")
ax3.legend(loc="best")

ax4.set_visible(False)

plt.show()


fig,(ax1,ax2) = plt.subplots(2,1, figsize=(9,4))
ax1.plot(freq1[mask1],data1_fft[mask1] , 'r-', label='diff-data1')
ax1.plot(freq2[mask2],data2_fft[mask2] , 'b-', label='diff-data2')
ax1.plot(freq3[mask3],data3_fft[mask3] , 'y-', label='diff-data3')
ax1.set_ylabel("meas(u.a.)")
ax1.set_xlabel("time(s)")

ax2.plot(freq1[mask1],y_fit_data1[mask1] , 'r-', label='fit-data1')
ax2.plot(freq2[mask2],y_fit_data2[mask2], 'b-', label='fit-data2')
ax2.plot(freq3[mask3],y_fit_data3[mask3] , 'y-', label='fit-data3')
ax2.set_ylabel("meas(u.a.)")
ax2.set_xlabel("time(s)")

plt.suptitle("differences between fit and real data")
ax1.legend(loc="best")
ax2.legend(loc="best")
plt.show()

