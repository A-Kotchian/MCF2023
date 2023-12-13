
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
from funzioni import random_walk_phi,spost,random_walk_phi_cost



b=input("Vuoi il caso phi? (y/n)\n")
if b=="y":

    b=input("Vuoi vedere la traiettoria? (y/n)\n")
    if b=="y":
        
        primo = random_walk_phi(1,1000)
        secondo= random_walk_phi(1,1000)
        terzo = random_walk_phi(1,1000)   
        quarto= random_walk_phi(1,1000)
        quinto= random_walk_phi(1,1000)  

        fig, ((ax1,ax2),(ax3,ax4),(ax5,ax6)) = plt.subplots(3,2, figsize=(10, 20))

        ax1.plot(primo[0], primo[1])
        ax2.plot(secondo[0], secondo[1])
        ax3.plot(terzo[0], terzo[1])
        ax4.plot(quarto[0], quarto[1])
        ax5.plot(quinto[0], quinto[1])
        ax6.set_visible(False)

        ax1.set_xlabel('Delta X')
        ax1.set_ylabel('Delta Y')

        ax2.set_xlabel('Delta X')
        ax2.set_ylabel('Delta Y')

        ax3.set_xlabel('Delta X')
        ax3.set_ylabel('Delta Y')

        ax4.set_xlabel('Delta X')
        ax4.set_ylabel('Delta Y')

        ax5.set_xlabel('Delta X')
        ax5.set_ylabel('Delta Y')

        plt.show()

    b=input("Vuoi vedere per 100 cristiani la traiettoria? (y/n)\n")

    if b=="y":
        
        dieci=np.array([0])
        cento=np.array([0])
        mille=np.array([0])

        for i in range(0,100):
            final = random_walk_phi(1, 10)
            x_pos, y_pos = final[0][-1], final[1][-1]
            dieci = np.append(dieci, [x_pos, y_pos])

        for i in range(0,100):
            final = random_walk_phi(1, 100)
            x_pos, y_pos = final[0][-1], final[1][-1]
            cento = np.append(cento, [x_pos, y_pos])

        for i in range(0,100):
            final = random_walk_phi(1, 1000)
            x_pos, y_pos = final[0][-1], final[1][-1]
            mille = np.append(mille, [x_pos, y_pos])
        

        fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2, figsize=(10, 20))

        for i in range(0,100):
            ax1.plot(dieci[i], dieci[i+1],".")
            ax2.plot(cento[i], cento[i+1],".")
            ax3.plot(mille[i], mille[i+1],".")
        ax4.set_visible(False)
        ax1.set_title("10")
        ax1.set_xlabel('Delta X')
        ax1.set_ylabel('Delta Y')
        ax2.set_title("100")
        ax2.set_xlabel('Delta X')
        ax2.set_ylabel('Delta Y')
        ax3.set_title("1000")
        ax3.set_xlabel('Delta X')
        ax3.set_ylabel('Delta Y')

        plt.show()


    b=input("Vuoi vedere per la traiettoria e la distanza? (y/n)\n")

    if b =="y":

        primo = random_walk_phi_cost(1,1000)
        secondo= random_walk_phi(1,1000)
        terzo = random_walk_phi(1,1000)   
        quarto= random_walk_phi(1,1000)
        quinto= random_walk_phi(1,1000)  

        fig, ((ax1,ax2),(ax3,ax4),(ax5,ax6)) = plt.subplots(3,2, figsize=(10, 20))

        ax1.plot(primo[0], primo[1],".")
        ax2.plot(secondo[0], secondo[1],".")
        ax3.plot(terzo[0], terzo[1],".")
        ax4.plot(quarto[0], quarto[1],".")
        ax5.plot(quinto[0], quinto[1],".")
        ax6.set_visible(False)

        ax1.set_xlabel('Delta X')
        ax1.set_ylabel('Delta Y')

        ax2.set_xlabel('Delta X')
        ax2.set_ylabel('Delta Y')

        ax3.set_xlabel('Delta X')
        ax3.set_ylabel('Delta Y')

        ax4.set_xlabel('Delta X')
        ax4.set_ylabel('Delta Y')

        ax5.set_xlabel('Delta X')
        ax5.set_ylabel('Delta Y')

        plt.show()

        spost_primo=(spost(primo[0],primo[1]))
        spost_secondo=spost(secondo[0],secondo[1])
        spost_terzo=(spost(terzo[0],terzo[1]))
        spost_quarto=(spost(quarto[0],quarto[1]))
        spost_quinto=(spost(quinto[0],quinto[1]))


        fig, ((ax1,ax2),(ax3,ax4),(ax5,ax6)) = plt.subplots(3,2, figsize=(10, 20))

        ax1.plot(spost_primo[0], spost_primo[1])
        ax2.plot(spost_secondo[0], spost_secondo[1])
        ax3.plot(spost_terzo[0], spost_terzo[1])
        ax4.plot(spost_quarto[0], spost_quarto[1])
        ax5.plot(spost_quinto[0], spost_quinto[1])
        ax6.set_visible(False)



        ax1.set_xlabel('Delta X')
        ax1.set_ylabel('Delta Y')

        ax2.set_xlabel('Delta X')
        ax2.set_ylabel('Delta Y')

        ax3.set_xlabel('Delta X')
        ax3.set_ylabel('Delta Y')

        ax4.set_xlabel('Delta X')
        ax4.set_ylabel('Delta Y')

        ax5.set_xlabel('Delta X')
        ax5.set_ylabel('Delta Y')

        plt.show()


        print("\nLa distanza inizio-fine per il primo è: (",spost_primo[0][-1]-spost_primo[0][0]," , " ,spost_primo[1][-1]-spost_primo[1][0],")")
        print("\nLa distanza inizio-fine per il secondo è: (",spost_secondo[0][-1]-spost_secondo[0][0]," , " ,spost_secondo[1][-1]-spost_secondo[1][0],")")
        print("\nLa distanza inizio-fine per il terzo è: (",spost_terzo[0][-1]-spost_terzo[0][0]," , " ,spost_terzo[1][-1]-spost_terzo[1][0],")")
        print("\nLa distanza inizio-fine per il quarto è: (",spost_quarto[0][-1]-spost_quarto[0][0]," , " ,spost_quarto[1][-1]-spost_quarto[1][0],")")
        print("\nLa distanza inizio-fine per il quinto è: (",spost_quinto[0][-1]-spost_quinto[0][0]," , " ,spost_quinto[1][-1]-spost_quinto[1][0],")")


b=input("Vuoi il caso moltiplicativo? (y/n): \n")
if b=="y":
    b=input("Vuoi vedere la traiettoria? (y/n)\n")
    if b=="y":
        
        primo = random_walk_phi_cost(1,1000,1)
        secondo= random_walk_phi_cost(1,1000,1)
        terzo = random_walk_phi_cost(1,1000,1)   
        quarto= random_walk_phi_cost(1,1000,1)
        quinto= random_walk_phi_cost(1,1000,1)  

        fig, ((ax1,ax2),(ax3,ax4),(ax5,ax6)) = plt.subplots(3,2, figsize=(10, 20))

        ax1.plot(primo[0], primo[1])
        ax2.plot(secondo[0], secondo[1])
        ax3.plot(terzo[0], terzo[1])
        ax4.plot(quarto[0], quarto[1])
        ax5.plot(quinto[0], quinto[1])
        ax6.set_visible(False)

        ax1.set_xlabel('Delta X')
        ax1.set_ylabel('Delta Y')

        ax2.set_xlabel('Delta X')
        ax2.set_ylabel('Delta Y')

        ax3.set_xlabel('Delta X')
        ax3.set_ylabel('Delta Y')

        ax4.set_xlabel('Delta X')
        ax4.set_ylabel('Delta Y')

        ax5.set_xlabel('Delta X')
        ax5.set_ylabel('Delta Y')

        plt.show()

    b=input("Vuoi vedere per 100 cristiani la traiettoria? (y/n)\n")

    if b=="y":
        
        dieci=np.array([0])
        cento=np.array([0])
        mille=np.array([0])

        for i in range(0,100):
            final = random_walk_phi_cost(1, 10,1)
            x_pos, y_pos = final[0][-1], final[1][-1]
            dieci = np.append(dieci, [x_pos, y_pos])

        for i in range(0,100):
            final = random_walk_phi_cost(1, 100,1)
            x_pos, y_pos = final[0][-1], final[1][-1]
            cento = np.append(cento, [x_pos, y_pos])

        for i in range(0,100):
            final = random_walk_phi_cost(1, 1000,1)
            x_pos, y_pos = final[0][-1], final[1][-1]
            mille = np.append(mille, [x_pos, y_pos])
        

        fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2, figsize=(10, 20))

        for i in range(0,100):
            ax1.plot(dieci[i], dieci[i+1],".")
            ax2.plot(cento[i], cento[i+1],".")
            ax3.plot(mille[i], mille[i+1],".")
        ax4.set_visible(False)
        ax1.set_title("10")
        ax1.set_xlabel('Delta X')
        ax1.set_ylabel('Delta Y')
        ax2.set_title("100")
        ax2.set_xlabel('Delta X')
        ax2.set_ylabel('Delta Y')
        ax3.set_title("1000")
        ax3.set_xlabel('Delta X')
        ax3.set_ylabel('Delta Y')

        plt.show()


    b=input("Vuoi vedere per la traiettoria e la distanza? (y/n)\n")

    if b =="y":

        primo = random_walk_phi_cost(1,1000,1)
        secondo= random_walk_phi_cost(1,1000,1)
        terzo = random_walk_phi_cost(1,1000,1)   
        quarto= random_walk_phi_cost(1,1000,1)
        quinto= random_walk_phi_cost(1,1000,1)  

        fig, ((ax1,ax2),(ax3,ax4),(ax5,ax6)) = plt.subplots(3,2, figsize=(10, 20))

        ax1.plot(primo[0], primo[1],".")
        ax2.plot(secondo[0], secondo[1],".")
        ax3.plot(terzo[0], terzo[1],".")
        ax4.plot(quarto[0], quarto[1],".")
        ax5.plot(quinto[0], quinto[1],".")
        ax6.set_visible(False)

        ax1.set_xlabel('Delta X')
        ax1.set_ylabel('Delta Y')

        ax2.set_xlabel('Delta X')
        ax2.set_ylabel('Delta Y')

        ax3.set_xlabel('Delta X')
        ax3.set_ylabel('Delta Y')

        ax4.set_xlabel('Delta X')
        ax4.set_ylabel('Delta Y')

        ax5.set_xlabel('Delta X')
        ax5.set_ylabel('Delta Y')

        plt.show()

        spost_primo=(spost(primo[0],primo[1]))
        spost_secondo=spost(secondo[0],secondo[1])
        spost_terzo=(spost(terzo[0],terzo[1]))
        spost_quarto=(spost(quarto[0],quarto[1]))
        spost_quinto=(spost(quinto[0],quinto[1]))


        fig, ((ax1,ax2),(ax3,ax4),(ax5,ax6)) = plt.subplots(3,2, figsize=(10, 20))

        ax1.plot(spost_primo[0], spost_primo[1])
        ax2.plot(spost_secondo[0], spost_secondo[1])
        ax3.plot(spost_terzo[0], spost_terzo[1])
        ax4.plot(spost_quarto[0], spost_quarto[1])
        ax5.plot(spost_quinto[0], spost_quinto[1])
        ax6.set_visible(False)



        ax1.set_xlabel('Delta X')
        ax1.set_ylabel('Delta Y')

        ax2.set_xlabel('Delta X')
        ax2.set_ylabel('Delta Y')

        ax3.set_xlabel('Delta X')
        ax3.set_ylabel('Delta Y')

        ax4.set_xlabel('Delta X')
        ax4.set_ylabel('Delta Y')

        ax5.set_xlabel('Delta X')
        ax5.set_ylabel('Delta Y')

        plt.show()


        print("\nLa distanza inizio-fine per il primo è: (",spost_primo[0][-1]-spost_primo[0][0]," , " ,spost_primo[1][-1]-spost_primo[1][0],")")
        print("\nLa distanza inizio-fine per il secondo è: (",spost_secondo[0][-1]-spost_secondo[0][0]," , " ,spost_secondo[1][-1]-spost_secondo[1][0],")")
        print("\nLa distanza inizio-fine per il terzo è: (",spost_terzo[0][-1]-spost_terzo[0][0]," , " ,spost_terzo[1][-1]-spost_terzo[1][0],")")
        print("\nLa distanza inizio-fine per il quarto è: (",spost_quarto[0][-1]-spost_quarto[0][0]," , " ,spost_quarto[1][-1]-spost_quarto[1][0],")")
        print("\nLa distanza inizio-fine per il quinto è: (",spost_quinto[0][-1]-spost_quinto[0][0]," , " ,spost_quinto[1][-1]-spost_quinto[1][0],")")
    b=input("Vuoi vedere la traiettoria con diversi moltiplicatori? (y/n)\n")
    if b=="y":
        molt=input("\nA quanto lo vuoi?\n")
        primo = random_walk_phi_cost(1,1000,molt)
        secondo= random_walk_phi_cost(1,1000,molt)
        terzo = random_walk_phi_cost(1,1000,molt)   
        quarto= random_walk_phi_cost(1,1000,molt)
        quinto= random_walk_phi_cost(1,1000,molt)  

        fig, ((ax1,ax2),(ax3,ax4),(ax5,ax6)) = plt.subplots(3,2, figsize=(10, 20))

        ax1.plot(primo[0], primo[1])
        ax2.plot(secondo[0], secondo[1])
        ax3.plot(terzo[0], terzo[1])
        ax4.plot(quarto[0], quarto[1])
        ax5.plot(quinto[0], quinto[1])
        ax6.set_visible(False)

        ax1.set_xlabel('Delta X')
        ax1.set_ylabel('Delta Y')

        ax2.set_xlabel('Delta X')
        ax2.set_ylabel('Delta Y')

        ax3.set_xlabel('Delta X')
        ax3.set_ylabel('Delta Y')

        ax4.set_xlabel('Delta X')
        ax4.set_ylabel('Delta Y')

        ax5.set_xlabel('Delta X')
        ax5.set_ylabel('Delta Y')

        plt.show()
