import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.integrate as integrate
import scipy.optimize as optimize
import math
from scipy import stats



def gauss(massa,a,b,c,x,sigma):
    return a*np.exp(-(x-massa)**2/(2*sigma**2))+b*x+c


def gauss2(massa,a1,a2,b,c,x,sigma1,sigma2):
    return a1*np.exp(-(x-massa)**2/(2*sigma1**2))+a2*np.exp(-(x-massa)**2/(2*sigma2**2))+b*x+c

dataset=pd.read_csv("/home/alessandro/Metodi-Computazionali/22_11_23/Jpsimumu.csv")


dataset 


c=300 

E1=dataset["E1"]
E2=dataset["E2"]

run=dataset["Run"]
Event=dataset["Event"]

px1=dataset["px1"]
py1=dataset["py1"]
pz1=dataset["pz1"]

eta1=dataset["eta1"]
phi1=dataset["phi1"]
Q1=dataset["Q1"]

type2=dataset["type2"]

px2=dataset["px2"]
py2=dataset["py2"]
pz2=dataset["pz2"]

eta2=dataset["eta2"]
phi2=dataset["phi2"]
Q2=dataset["Q2"]


massa1=np.sqrt((E1)**2-((px1)**2+(py1)**2+(pz1)**2))
massa2=np.sqrt((E2)**2-((px2)**2+(py2)**2+(pz2)))
massa_dec=np.sqrt((E1+E2)**2-((px1+px2)**2+(py1+py2)**2+(pz1+pz2)**2))


mask=np.logical_and(massa_dec>3.4, massa_dec<4)
massa_int=massa_dec[mask]



fig,ax=plt.subplots(figsize=(10,7))

ins=ax.inset_axes([0.6,0.5,0.32,0.37])
n,p,bins=ins.hist(massa_int, bins=200,range=(3.4,4),color="gold")
ins.set_xlabel("mc^2(GeVm^2/s^2)")
ins.set_ylabel("Events/3GeV")
ins.set_title("Focus on range [3.0-3.2]")


plt.hist(massa_dec, bins=200,range=(2,5), color="navajowhite")
#plt.suptitle("Dati CMS: sqrt(s)= 7TeV, L= 5.1 fb^-1 ")
plt.title("Dati CMS: sqrt(s)= 7TeV, L= 5.1 fb^-1 ")
plt.xlabel("mc^2(mGeV/s^2)")
plt.ylabel("Events/3GeV")
plt.show()


print(p)
p_centers= (p[:-1]+p[1:])/2
err_n=np.sqrt(n)
print(n)

"""
print(len(n))
print(len(p))
print(len(bins))
print(massa_dec)
"""


#n,p,bins=plt.hist(massa_int, bins=200,range=(3.0,3.75))
b=input("\nVuoi vedere la gaussiana singola?\n")
if(int(b)==1):

    params,params_covariance =optimize.curve_fit(gauss,xdata=p_centers,ydata=n, sigma=err_n )



    #chi_2_1=stats.chisquare(p_centers,gauss(n,params[0],params[1],params[2],params[3],params[4])) #)
    err=np.sqrt(np.diag(params_covariance))
    y_fit = gauss(p_centers,params[0],params[1],params[2],params[3],params[4])
    df = len(p_centers)-len(params)
    chi2 =  np.sum( (y_fit - n)**2 /n )
    prob = stats.chi2.sf(chi2, df)
    print("\n----------------------------------------------\n")
    #print("\nchi",chi_2_1)
    print("\nChi2: ", chi2)
    print("\nChi ridotto",chi2/df)
    print("\nProbability",prob)
    #print('\nParams', params )
    #print('\nparams_cov', params_covariance)
    #print('1nerrori params', np.sqrt(params_covariance.diagonal()))
    print("\n----------------------------------------------\n")



    fig, ax = plt.subplots(2,1, figsize=(9,6), gridspec_kw={'height_ratios': [3, 1]}, sharex=True)
    fig.subplots_adjust(hspace=0)
    ax[1].errorbar(p_centers,(y_fit - n ),yerr=err_n,fmt ="o")
    ax[1].set_ylabel('Dati/Fit',  fontsize =14)
    ax[1].tick_params(axis="x",   labelsize=14) 
    ax[1].tick_params(axis="y",   labelsize=14)
    ax[1].axhline(0,color="green",alpha=0.4)
    ax[1].axhline(25,color="green",alpha=0.4)
    ax[1].axhline(-25,color="green",alpha=0.4)
    ax[0].plot(p_centers,gauss(p_centers,params[0],params[1],params[2],params[3],params[4]),"-",color="darkolivegreen")
    ax[0].hist(massa_int, bins=200,range=(3.4,4),color="goldenrod",alpha=0.7)
    fig.suptitle("Fit picco centrale Gaussiana singola: sqrt(s)= 7TeV, L= 5.1 fb^-1 ")
    ax[0].set_xlabel("mc^2(mGeV/s^2)")
    ax[0].set_ylabel("Events/3GeV")
    plt.show()

    print("La probabilita che fitta bene è : ", round((prob)*100,3) ," %")


b=input("\nVuoi vedere la gaussiana doppia?\n")
if(int(b)==1):

    params,params_covariance =optimize.curve_fit(gauss2,xdata=p_centers,ydata=n, sigma=err_n)
    err=np.sqrt(np.diag(params_covariance))
    y_fit = gauss2(p_centers,params[0],params[1],params[2],params[3],params[4],params[5],params[6])
    df = len(p_centers)-len(params)

    chi2 =  np.sum( (y_fit - n)**2 /n )

    prob = stats.chi2.cdf(chi2, df)
    print("\n----------------------------------------------\n")
    #print("\nchi",chi_2_1)
    print("\nChi2: ", chi2)
    print("\nChi ridotto",chi2/df)
    print("\nProbability",1-prob)
    
    #print('\nParams', params )
    #print('\nparams_cov', params_covariance)
    #print('1nerrori params', np.sqrt(params_covariance.diagonal()))
    print("\n----------------------------------------------\n")



    fig, ax = plt.subplots(2,1, figsize=(9,6), gridspec_kw={'height_ratios': [3, 1]}, sharex=True)
    fig.subplots_adjust(hspace=0)
    fig.suptitle("Fit picco centrale Gaussiana singola: sqrt(s)= 7TeV, L= 5.1 fb^-1 ")
    ax[1].errorbar(p_centers,(y_fit - n ),yerr=err_n,fmt ="o")
    ax[1].set_ylabel('Dati/Fit',  fontsize =14)
    ax[1].tick_params(axis="x",   labelsize=14) 
    ax[1].tick_params(axis="y",   labelsize=14)
    ax[1].axhline(0,color="green",alpha=0.4)
    ax[1].axhline(25,color="green",alpha=0.4)
    ax[1].axhline(-25,color="green",alpha=0.4)
    ax[0].plot(p_centers,gauss2(p_centers,params[0],params[1],params[2],params[3],params[4],params[5],params[6]),"-",color="darkolivegreen")
    ax[0].hist(massa_int, bins=200,range=(3.4,4),color="red",alpha=0.4)
    ax[0].set_xlabel("mc^2(mGeV/s^2)")
    ax[0].set_ylabel("Events/3GeV")
    plt.show()

    print("La probabilita che fitta bene è : ", round((1-prob)*100,3) ," %")
