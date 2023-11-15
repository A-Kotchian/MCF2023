import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.integrate as integrate

import sys,os
import argparse


def parse_arguments():
    
    parser = argparse.ArgumentParser(description='Esempio utilizzo argarse.',
                                     usage      ='python3 argparse_example.py  --opzione')
    parser.add_argument('-1', '--primo',    action='store_true',                     help='Primo grafico')
    parser.add_argument('-2', '--secondo',    action='store_true',                          help='Secondo grafico')
    return  parser.parse_args()


def main():
    file=pd.read_csv("/home/alessandro/Metodi-Computazionali/15_11_23/vel_vs_time.csv")

    tempi=file["t"]
    velocita=file["v"]

    inip=[]
    integr=integrate.simpson(velocita,tempi)
    for i in range(1,len(tempi)+1):
        inip.append(integrate.simpson(velocita[:i+1],tempi[:i+1],dx=tempi[2]-tempi[1]))


    args = parse_arguments()

    # print 
    #print(args)

    if args.primo == True :
        print('---------------------------------------------')
        print("---------------------------------------------")
        plt.plot(tempi,velocita)
        plt.xlabel('Tempo (s)')
        plt.ylabel('Velocità (m/s)')
        plt.show()
        print('---------------------------------------------')

    if args.secondo == True :
        print('---------------------------------------------')
        plt.plot(tempi, inip)
        plt.xlabel('Tempo (s)')
        plt.ylabel('Distanza (m)')
        plt.show()
        print('---------------------------------------------')




if __name__ == "__main__":

    main()
