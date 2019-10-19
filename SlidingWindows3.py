# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 17:48:41 2019

@author: Tiago Ibacache
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as waves


Archivo1 = 'Recorte_1.wav'
Archivo2 = 'Recorte_2.wav'
#Frec1 = waves.read(Archivo1)
#Frec2 = waves.read(Archivo2)
Frec1, ASon1 = waves.read(Archivo1)
Frec2, ASon2 = waves.read(Archivo2)
tamano1 = np.shape(ASon1)
tamano2 = np.shape(ASon2)
TamEnSeg1 = len(tamano1)
TamEnSeg2 = len(tamano2)
TamSon1 = len(ASon1)
TamSon2 = len(ASon2)
#Comp = (Frec1==Frec2).all()
#repetidos = []
#Diferencia = (Frec1 - Frec2) 
    
"""def DEF(F1, F2):
    (F1==F2).all()
    print("Son los mismos archivos")
   # else:
       # Diferencia = (Frec1 - Frec2)
    #    print ('Las frecuencias son distintas, la diferencia es : ')
        
DEF(Frec1, Frec2)


for x in Frec1:
    for y in Frec2:
        if x == y:
            repetidos.append(x)
"""

print('Vamos a comparar dos archivos de audio de un segundo cada uno, cada calcularemos la Frecuencia, la magnitud, etc')

def CompTamEnSeg(TES1, TES2):
    if (TES1 == TES2):
        print('Son de igual tamaño en segundos')
    else:
        print('Hay una diferencia de', TES1 - TES2)
        
def CompTam(T1, T2):
    if (T1 == T2):
        print('Son de igual tamaño')
    else:
        print('Es la diferencia de tamaño')
        
def CompFrec(F1, F2):
    if (F1 == F2):
        print('Son iguales')
    else:
        print('Es la diferencia de frecuencias')
        
def CompASon(AS1, AS2):
    if (AS1[20] == AS2[20]):
                print('Coinciden en: ')
    else:
        print('No coincice el array')
          
CompASon(ASon1, ASon2)
CompTamEnSeg(TamEnSeg1, TamEnSeg2)
CompFrec(Frec1, Frec2)
CompTam(tamano1, tamano2)