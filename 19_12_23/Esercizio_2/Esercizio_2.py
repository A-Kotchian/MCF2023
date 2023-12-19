import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.integrate as integrate
import mycamera
import ctypes
import sys


class myCamera:

    def __init__(self):
        self.ciaone=0

    def read_camera(self):
        buffer=mycamera.read_camera()
        return buffer
    def decodifica(self):
        buffer=self.read_camera()
        image=[]
        for i in range(0,1024):
            pippolo=[]
            for j in range(0,1536):
                pippolo.append(int.from_bytes(buffer[i*3072+2*j]+buffer[i*3072+2*j+1],byteorder="little",signed="False"))    #(*)
            image.append(pippolo)
        return image
    
    def visualizza(self,image):
        plt.imshow(image, cmap='copper',norm="log",origin='lower')
        plt.show()

    def visualizzatore(self,colore,norma):
        width = 1536
        height = 1024
        buffer=self.read_camera()
        image_buffer = np.frombuffer(buffer, dtype=np.uint16)            
        image = image_buffer.reshape((height, width))
        plt.imshow(image, cmap=colore,norm=norma,origin='lower')
        plt.show() 
    def foto(self,image):
        plt.imshow(image, cmap='copper',norm="log",origin='lower')
        plt.savefig("image.png",format="png")



# buffer=mycamera.read_camera()

# image=[]
# for i in range(0,1024):
#     pippolo=[]
#     for j in range(0,1536):
#         pippolo.append(int.from_bytes(buffer[i*3072+2*j]+buffer[i*3072+2*j+1],byteorder="little",signed="False"))    #(*)
#     image.append(pippolo)


# plt.imshow(image, cmap='copper',norm="log",origin='lower')
# plt.show()


print("Benvenuto nel visualizzatore di buffer\nCome posso aiutarti?\n")

camerina=myCamera()
print("----------------------------------------------------------------------------------------------------------------")

a=input("1)Leggi dalla camera\n2)Decodifica\n3)Visualizza\n4)Visualizza con norma e colore\n5)Salva immagine\n0)Esci\n----------------------------------------------------------------------------------------------------------------\n")
b=int(a)


if(b==1):
    camerina.read_camera()
    print("Fatto!\n")

if(b==2):
    camerina.decodifica()
    print("Fatta la decodifica!\n")

if(b==3):
    image=camerina.decodifica()
    camerina.visualizza(image)

if(b==4):
    norm=input("Dimmi che norma vuoi:\n")
    colore=input("Dimmi che colore vuoi:\n")
    camerina.visualizzatore(colore,norm)

if(b==5):
    image=camerina.decodifica()
    camerina.foto(image)
    print("Immagine salvata!\n")






