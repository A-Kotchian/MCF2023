import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sympy 




df = pd.read_csv("18_10_23/get-mcf-data-main/4LAC_DR2_sel.csv")

print("Il nome delle colonne sono:\n")

col=df.columns

for i in col:
    print("- ",i)
    

print(df.head())

PL = df["PL_Index"]
flusso = df["Flux1000"]                 #prendo colonne del dataframe
er_flusso = df["Unc_Flux1000"]
nu_syn=df["nu_syn"]




#sotto dataframe
log10_=df.loc[ (df['nu_syn']>0)]

log10_er_PL=log10_['Unc_PL_Index']
log10_nu_syn=np.log10(log10_["nu_syn"])               #sotto-classe
log10_PL=log10_["PL_Index"]


#suddivisione dataframe log10_

##bll

bll=log10_.loc[ (log10_['CLASS']=="bll")]
bll_er_PL=bll['Unc_PL_Index']
bll_nu_syn=bll["nu_syn"]                          #sotto-sotto-classe 
bll_PL=bll["PL_Index"]



##fsrq

fsrq=log10_.loc[ (log10_['CLASS']=="fsrq")]
fsrq_er_PL=fsrq['Unc_PL_Index']                     #sotto-sotto-classe 
fsrq_nu_syn=fsrq["nu_syn"]
fsrq_PL=fsrq["PL_Index"]



a=input("Li vediamo?")

if(a==1):
    f1 = plt.figure(1)

    plt.scatter( flusso,PL, color='royalblue', s=16)

    plt.ylabel('PL_Index', fontsize=16)
    plt.xlabel('Flux1000 (cm^(-2)s^(-1))', fontsize=16)         #es 4
    plt.show()


    f2 = plt.figure(2)
    plt.scatter( flusso,PL, color='lime', s=16)

    plt.ylabel('PL_Index', fontsize=16)
    plt.xlabel('logFlux1000 (cm^(-2)s^(-1))', fontsize=16)      #es 5
    plt.xscale("log")
    plt.show()


    f3 = plt.figure(3)
    plt.scatter( log10_nu_syn,log10_PL, color='lightgray', s=16)

    plt.ylabel('log10_PL_Index', fontsize=16)
    plt.xlabel('log10_nu_syn (Hz)', fontsize=16)            #es 6
    plt.xscale("log")



    f4 = plt.figure(4)
    plt.scatter( np.log10(bll_nu_syn),bll_PL, color='red', s=16,alpha=0.5)
    plt.scatter( np.log10(fsrq_nu_syn),fsrq_PL, color='yellow', s=16,alpha=0.4)

    plt.ylabel('log10_PL_Index', fontsize=16)
    plt.xlabel('log10_nu_syn(Hz) ', fontsize=16)
    plt.xscale("log")                               #es 7
    plt.legend(["bll","fsrq"])


    f5 = plt.figure(5)
    plt.errorbar( np.log10(bll_nu_syn),bll_PL,yerr=bll_er_PL,fmt=".", color='red',alpha=0.3)
    plt.errorbar( np.log10(fsrq_nu_syn),fsrq_PL,yerr=fsrq_er_PL,fmt="." ,color='yellow',alpha=0.3)

    plt.ylabel('log10_PL_Index', fontsize=16)
    plt.xlabel('log10_nu_syn (Hz)', fontsize=16)
    plt.xscale("log")                                   #es 8
    plt.legend(["bll","fsrq"])


    f6 = plt.figure(6)    #es 9
    n_fsrq, bis_fsrq, p_fsrq = plt.hist(fsrq_PL, bins=50,range=(1,4) ,color='blue', alpha=0.2 )
    n_bll, bis_bll, p_bll = plt.hist(bll_PL, bins=59,range=(1,4), color='green', alpha=0.2 )



    plt.xlabel('log10_PL_Index', fontsize=16)
    plt.legend(["bll","fsrq"])

    f7 = plt.figure(7)
    plt.hist(np.log10(bll_nu_syn), bins=40 ,range=(10,25),color='blue', alpha=0.2 )
    plt.hist(np.log10(fsrq_nu_syn), bins=40 ,range=(10,25),color='blue', alpha=0.2 )

    plt.xlabel('log10_nu_syn (Hz)', fontsize=16)                    #es 10
    plt.legend(["bll","fsrq"])


    plt.show()




x=0
y=0

fig = plt.figure()           #mi premette di creare una figura 
gs = fig.add_gridspec(2, 2, hspace=0, wspace=0)   #crea la figura della griglia

(ax1,ax2),(ax3,ax4)= gs.subplots(sharex="col",sharey="row")


ax3.scatter( np.log10(bll_nu_syn),bll_PL, color='red',s=16,alpha=0.5)
ax3.scatter( np.log10(fsrq_nu_syn),fsrq_PL, color='yellow', s=16,alpha=0.4)
ax3.set_xlim(9,22)
ax3.set_ylim(1,4)                                                 #grafico ax3
ax3.legend(["bll","fsrq"])



ax4.hist(fsrq_PL, bins=50,range=(1,4) ,color='blue', alpha=0.2 , orientation="horizontal")
ax4.hist(bll_PL, bins=59,range=(1,4), color='green', alpha=0.2 , orientation="horizontal")  #grafico ax4
ax4.legend(["bll","fsrq"])


ax3.sharey(ax4)
ax3.sharex(ax1)     #condivisione assi


ax1.set_ylabel("Number of sources")
ax3.set_xlabel("log(nu_sin [Hz])")
ax3.set_ylabel("PL Index") 
ax4.set_xlabel("Number of sources")   #condivisione 


ax1.hist(np.log10(bll_nu_syn), bins=40 ,range=(10,25),color='blue', alpha=0.2 )
ax1.hist(np.log10(fsrq_nu_syn), bins=40 ,range=(10,25),color='blue', alpha=0.2 )   #grafico ax1
ax1.legend(["bll","fsrq"])


ax2.set_visible(False) #non ti fa vedere il grafico 


ax2.plot(x + 2, y + 2)



plt.savefig("foto/Grafico_esercizio_2.png",format="png")  #salva il grafico con una foto nella cartella

plt.show()


df




